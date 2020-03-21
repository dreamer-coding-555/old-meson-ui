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
import re


class KDevelopBackend(BackendImpl):
    def __init__(self, meson_api: MesonAPI):
        super(self.__class__, self).__init__(meson_api)
        self.backend: str = 'KDevelop IDE'
        self.project_name = re.sub(r'[^a-z0-9]', '_', self.projectinfo['descriptive_name'])
        self.source: str = self.mesoninfo['directories']['source']
        self.build: str = self.mesoninfo['directories']['build']
        self.includes: list = []
        self.defines: list = []
        self.files: list = []

    def generator(self):
        logging.info(f'Generating {self.backend} project')

        # Generate the .kdev4 file.
        with open(join_paths(self.build, f'{self.project_name}.kdev4'), 'w') as file:
            file.write('[Project]\n')
            file.write(f'Name={self.project_name}\n')
            file.write('Manager=Meson\n')
