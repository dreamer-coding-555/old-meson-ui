#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.repository.mesonapi import MesonAPI
from .backendimpl import BackendImplementionApi
from os.path import join as join_paths
import logging
import os
import re


class QtCreatorBackend(BackendImplementionApi):
    def __init__(self, meson_api: MesonAPI):
        super(self.__class__, self).__init__(meson_api)
        self.backend: str = '\'qtcreator\''
        self.project_name = re.sub(r'[^a-z0-9]', '_', self.projectinfo['descriptive_name'])
        self.source: str = self.mesoninfo['directories']['source']
        self.build: str = self.mesoninfo['directories']['build']

    def generator(self):
        logging.info(f'Generating {self.backend} project')
        self.generate_project()

    def generate_project(self):
        # Generate the .creator file.
        with open(join_paths(self.build, f'{self.project_name}.creator'), 'w') as file:
            file.write('[General]')

        # Generate the .config file.
        with open(join_paths(self.build, f'{self.project_name}.config'), 'w') as file:
            file.write('// Add predefined macros for your project here. For example:')
            file.write('// #define THE_ANSWER 42')
            for targets in self.targetsinfo:
                for target in targets['target_sources']:
                    for item in target['parameters']:
                        if item.startswith('-D'):
                            logging.info(f'add def: {item}')
                            item = ' '.join(item.split('='))
                            file.write(f'#define {item}\n')

        # Generate the .files file.
        with open(join_paths(self.build, f'{self.project_name}.files'), 'w') as file:
            for targets in self.targetsinfo:
                for target in targets['target_sources']:
                    for item in target['sources']:
                        file.write(os.path.relpath(item, self.build) + '\n')

                    for item in self.buildsystem_files:
                        file.write(os.path.relpath(item, self.build) + '\n')

        # Generate the .includes file.
        with open(join_paths(self.build, f'{self.project_name}.includes'), 'w') as file:
            for targets in self.targetsinfo:
                for item in targets['target_sources']:
                    for item in target['parameters']:
                        if item.startswith('-I') or item.startswith('/I'):
                            file.write(os.path.relpath(item, self.build) + '\n')
