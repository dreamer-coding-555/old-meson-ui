#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.repository.mesonapi import MesonAPI
from pathlib import Path
import re


MESON_SUPPORTED_LANG: set = {'c', 'cpp', 'cs', 'cuda', 'd', 'fortran', 'java', 'rust', 'swift', 'vala', 'objc', 'objcpp'}


class MesonInfo:
    def __init__(self, meson_api: MesonAPI):
        self._meson_info: any = meson_api.get_object(group='meson-info', extract_method='loader')
        self.sourcedir: Path = Path(self._meson_info['directories']['source'])
        self.builddir: Path = Path(self._meson_info['directories']['build'])
        self.infodir: Path = Path(self._meson_info['directories']['info'])


class ProjectInfo:
    def __init__(self, meson_api: MesonAPI):
        self._project_info: any = meson_api.get_object(group='projectinfo', extract_method='loader')
        self.descriptive_name: str = re.sub(r'[^a-z0-9]', '_', self._project_info['descriptive_name'])
        self.subprojects: list = self._project_info['subprojects']
        self.number_of_subprojects: list = len(self._project_info['subprojects'])


class TargetsInfo:
    def __init__(self, meson_api: MesonAPI):
        self.targetsinfo: any = meson_api.get_object(group='targets', extract_method='loader')
        self.name = self._targets_info[0]['name']
        self.type = self._targets_info[0]['type']
        self.id = self._targets_info[0]['id']
        self.language = self._targets_info[0]['target_sources'][0]['language']
        self.compiler = self._targets_info[0]['target_sources'][0]['compiler']
        self.parameters = self._targets_info[0]['target_sources'][0]['parameters']
