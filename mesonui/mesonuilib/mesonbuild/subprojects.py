#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from pathlib import Path
import subprocess


class MesonSubprojects:
    def __init__(self, sourcedir: Path = None):
        self._sourcedir: Path = sourcedir
        super().__init__()

    def update(self, subproject):
        run_cmd = ['meson', 'subprojects', 'update', subproject, '--sourcedir', str(self._sourcedir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]

    def checkout(self, branch: str, subproject):
        run_cmd = ['meson', 'subprojects', 'checkout', branch, subproject, '--sourcedir', str(self._sourcedir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]

    def download(self, subproject):
        run_cmd = ['meson', 'subprojects', 'download', subproject, '--sourcedir', str(self._sourcedir)]
        process = subprocess.Popen(run_cmd, encoding='utf8', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return process.communicate()[0]
