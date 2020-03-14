#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from .mesonbuild.subprojects import MesonSubprojects
from .mesonbuild.configure import MesonConfigure
from .mesonbuild.install import MesonInstall
from .mesonbuild.version import MesonVersion
from .mesonbuild.compile import MesonCompile
from .mesonbuild.setup import MesonSetup
from .mesonbuild.build import MesonBuild
from .mesonbuild.clean import MesonClean
from .mesonbuild.init import MesonInit
from .mesonbuild.dist import MesonDist
from .mesonbuild.wrap import MesonWrap
from .mesonbuild.test import MesonTest

from os.path import join as join_paths
from pathlib import Path


class Meson:
    '''
    this class is a wrapper for the Meson build system.
    '''
    def __init__(self, sourcedir: Path = Path().cwd(), builddir: Path = join_paths(Path().cwd(), 'builddir')):
        super().__init__()
        self._sourcedir = sourcedir
        self._builddir = builddir
    # end of method

    @property
    def sourcedir(self):
        return self._sourcedir

    @property
    def builddir(self):
        return self._builddir

    @sourcedir.setter
    def sourcedir(self, new_dir: Path):
        self._sourcedir = new_dir

    @builddir.setter
    def builddir(self, new_dir: Path):
        self._builddir = new_dir

    def version(self) -> MesonVersion:
        return MesonVersion().run()

    def configure(self, args: list = []) -> MesonConfigure:
        return MesonConfigure(self.builddir).run(args=args)

    def setup(self, args: list = []) -> MesonSetup:
        return MesonSetup(self.sourcedir, self.builddir).run(args=args)

    def subprojects(self) -> MesonSubprojects:
        return MesonSubprojects(self.sourcedir)

    def compile(self, args: list = []) -> MesonCompile:
        return MesonCompile(self.builddir).run(args=args)

    def install(self, args: list = []) -> MesonInstall:
        return MesonInstall(self.builddir).run(args=args)

    def build(self) -> MesonBuild:
        return MesonBuild(self.builddir).run()

    def clean(self) -> MesonClean:
        return MesonClean(self.builddir).run()

    def init(self, args: list = []) -> MesonInit:
        return MesonInit(self.sourcedir).run(args=args)

    def dist(self, args: list = []) -> MesonDist:
        return MesonDist(self.builddir).run(args=args)

    def test(self) -> MesonTest:
        return MesonTest(self.builddir).run()

    def wrap(self) -> MesonWrap:
        return MesonWrap()
