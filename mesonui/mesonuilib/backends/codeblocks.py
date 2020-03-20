#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.repository.mesonapi import MesonAPI
from .backendimpl import BackendImpl
from os.path import join as join_paths
from ..buildsystem import Ninja
import logging
import os
import re
import xml.etree.ElementTree as ETree

BUILD_OPTION_EXECUTABLE = 1
BUILD_OPTION_STATIC_LIBRARY = 2
BUILD_OPTION_SHARED_LIBRARY = 3
BUILD_OPTION_COMMANDS_ONLY = 4
CBP_VERSION_MAJOR = 1
CBP_VERSION_MINOR = 6


class CodeBlocksBackend(BackendImpl):
    def __init__(self, meson_api: MesonAPI):
        super(self.__class__, self).__init__(meson_api)
        self.backend: str = 'Code::Blocks'
        self.compiler = self.targetsinfo[0]['target_sources'][0]['compiler'][0]
        self.project_name = re.sub(r'[^a-z0-9]', '_', self.projectinfo['descriptive_name'])
        self.source: str = self.mesoninfo['directories']['source']
        self.build: str = self.mesoninfo['directories']['build']
        self.ninja = Ninja(self.source, self.build)

    def generator(self):
        logging.info(f'Generating {self.backend} project')
        root = ETree.Element('CodeBlocks_project_file')
        tree = ETree.ElementTree(root)
        ETree.SubElement(root, 'FileVersion', {'major': f'{CBP_VERSION_MAJOR}', 'minor': f'{CBP_VERSION_MINOR}'})
        project = ETree.SubElement(root, 'Project')
        ETree.SubElement(project, 'Option', {'title': self.project_name})
        ETree.SubElement(project, 'Option', {'makefile_is_custom': '1'})
        ETree.SubElement(project, 'Option', {'compiler': self.compiler})
        ETree.SubElement(project, 'Option', {'virtualFolders': 'Meson Files'})

        build = ETree.SubElement(project, 'Build')

        for target in self.targetsinfo:
            build_target = ETree.SubElement(build, 'Target', {'title': target['name']})
            output = join_paths(self.build, target['id'])
            ETree.SubElement(build_target, 'Option', {'output': output})
            ETree.SubElement(build_target, 'Option', {'working_dir': os.path.split(output)[0]})
            ETree.SubElement(build_target, 'Option', {'object_output': join_paths(os.path.split(output)[0], target['id'])})
            ty = {
                'executable': f'{BUILD_OPTION_EXECUTABLE}',
                'static library': f'{BUILD_OPTION_STATIC_LIBRARY}',
                'shared library': f'{BUILD_OPTION_SHARED_LIBRARY}',
                'custom': f'{BUILD_OPTION_COMMANDS_ONLY}',
                'run': f'{BUILD_OPTION_COMMANDS_ONLY}'
            }[target['type']]
            ETree.SubElement(build_target, 'Option', {'type': ty})

            compiler = target
            if compiler:
                ETree.SubElement(build_target, 'Option', {'compiler': self.compiler})

            compiler = ETree.SubElement(build_target, 'Compiler')

            for define in target['target_sources'][0]['parameters']:
                if define.startswith('-D'):
                    ETree.SubElement(compiler, 'Add', {'option': define})

            for include_dir in target['target_sources'][0]['parameters']:
                if include_dir.startswith('-I') or include_dir.startswith('/I'):
                    ETree.SubElement(compiler, 'Add', {'directory': include_dir})

            make_commands = ETree.SubElement(build_target, 'MakeCommands')
            ETree.SubElement(make_commands, 'Build', {'command': f'{self.ninja.exe} -v {target["name"]}'})
            ETree.SubElement(make_commands, 'CompileFile', {'command': f'{self.ninja.exe} -v {target["name"]}'})
            ETree.SubElement(make_commands, 'Clean', {'command': f'{self.ninja.exe} -v clean'})
            ETree.SubElement(make_commands, 'DistClean', {'command': f'{self.ninja.exe} -v clean'})

        for target in self.targetsinfo:
            target_files = target['target_sources'][0]['sources']
            for target_file in target_files:
                unit = ETree.SubElement(project, 'Unit', {'filename': join_paths(self.source, target_file)})
                ETree.SubElement(unit, 'Option', {'target': target['name']})

                base = os.path.splitext(os.path.basename(target_file))[0]
                header_exts = ('h', 'hpp')
                for ext in header_exts:
                    header_file = os.path.abspath(
                        join_paths(self.source, os.path.dirname(target_file), join_paths(base + '.' + ext)))
                    if os.path.exists(header_file):
                        unit = ETree.SubElement(project, 'Unit', {'filename': header_file})
                        ETree.SubElement(unit, 'Option', {'target': target['name']})

        for file in self.buildfiles:
            unit = ETree.SubElement(project, 'Unit', {'filename': join_paths(self.source, file)})
            ETree.SubElement(unit, 'Option', {'virtualFolder': join_paths('Meson Files', os.path.dirname(file))})

        project_file = join_paths(self.build, f'{self.project_name}.cbp')
        tree.write(project_file, 'unicode', True)
