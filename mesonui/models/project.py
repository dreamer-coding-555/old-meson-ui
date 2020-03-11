#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from ..mesonuilib.buildsystem import Meson
from pathlib import Path


class ProjectModel:
    def __init__(self):
        super().__init__()
        self._sourcedir: Path = Path().cwd()
        self._builddir: Path = Path().joinpath(self._sourcedir, 'builddir')
        self._scriptdir: Path = Path().joinpath(self._sourcedir, 'meson.build')
        self._meson: Meson = Meson(self._sourcedir, self._builddir)

    def meson(self) -> Meson:
        return self._meson

    def get_scriptdir(self) -> Path:
        return self._scriptdir

    def get_sourcedir(self) -> Path:
        return self._sourcedir

    def get_builddir(self) -> Path:
        return self._builddir

    def set_scriptdir(self, value: Path) -> None:
        self._scriptdir = value

    def set_sourcedir(self, value: Path) -> None:
        self._sourcedir = value

    def set_builddir(self, value: Path) -> None:
        self._builddir = value
