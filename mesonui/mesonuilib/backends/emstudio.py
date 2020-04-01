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
from ..buildsystem import Meson
import logging
import re


class EmbeddedStudioBackend(BackendImplementionApi):
    def __init__(self, meson_api: MesonAPI):
        super(self.__class__, self).__init__(meson_api)
        self.backend: str = '\'emstudio\''
        self.project_name = re.sub(r'[^a-z0-9]', '_', self.projectinfo['descriptive_name'])
        self.source: str = self.mesoninfo['directories']['source']
        self.build: str = self.mesoninfo['directories']['build']
        self.meson = Meson()

    def generator(self):
        logging.info(f'Generating {self.backend} project')
        self.generate_project()

    def generate_project(self):
        pass
