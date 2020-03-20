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
import logging
import os
import re


class QtCreatorBackend(BackendImpl):
    def __init__(self, meson_api: MesonAPI):
        super(self.__class__, self).__init__(meson_api)
        self.backend: str = 'qtcreator'
        self.project_name = re.sub(r'[^a-z0-9]', '_', self.projectinfo['descriptive_name'])
        self.source: str = self.mesoninfo['directories']['source']
        self.build: str = self.mesoninfo['directories']['build']
        self.includes: list = []
        self.defines: list = []
        self.files: list = []

    def generator(self):
        logging.info(f'Generating {self.backend} project')

        # Generate the .creator file.
        with open(join_paths(self.build, f'{self.project_name}.creator'), 'w') as file:
            file.write('[General]')

        # Generate the .config file.
        with open(join_paths(self.build, f'{self.project_name}.config'), 'w') as file:
            file.write('// Add predefined macros for your project here. For example:')
            file.write('// #define THE_ANSWER 42')
            for item in self.defines:
                logging.info(f'defs: {item}')
                item = ' '.join(item.split('='))
                file.write(f'#define {item}\n')

        # Generate the .files file.
        self.files = self.targetsinfo[0]['target_sources'][0]['sources']
        self.files.extend(self.buildfiles)

        with open(join_paths(self.build, f'{self.project_name}.files'), 'w') as file:
            for item in self.files:
                logging.info(f'files: {item}')
                file.write(os.path.relpath(item, self.build) + '\n')

        # Generate the .includes file.
        parameters = self.targetsinfo[0]['target_sources'][0]['parameters']
        for i in range(len(parameters)):
            if parameters[i].startswith('-I') or parameters[i].startswith('/I'):
                logging.info(f'prams: {parameters[i]}')
                self.includes.extend([self.targetsinfo[0]['target_sources'][0]['parameters'][i]])

        with open(join_paths(self.build, f'{self.project_name}.includes'), 'w') as file:
            for item in self.includes:
                logging.info(f'includes: {item}')
                file.write(os.path.relpath(item, self.build) + '\n')
