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
from pathlib import Path
import typing as T


class Meson:
    '''
    this class is a wrapper for the Meson build system.
    '''
    def __init__(self, sourcedir: Path = Path().cwd(), builddir: Path = Path().joinpath(Path().cwd(), 'builddir')):
        super().__init__()
        self._subprojects: MesonSubprojects = MesonSubprojects(sourcedir)
        self._configure: MesonConfigure = MesonConfigure(builddir)
        self._install: MesonInstall = MesonInstall(builddir)
        self._version: MesonVersion = MesonVersion()
        self._compile: MesonCompile = MesonCompile(builddir)
        self._setup: MesonSetup = MesonSetup(sourcedir, builddir)
        self._build: MesonBuild = MesonBuild(builddir)
        self._clean: MesonClean = MesonClean(builddir)
        self._dist: MesonDist = MesonDist(builddir)
        self._init: MesonInit = MesonInit(sourcedir)
        self._test: MesonTest = MesonTest(builddir)
        self._wrap: MesonWrap = MesonWrap()
    # end of method

    def version(self) -> MesonVersion:
        return self._version.run()

    def configure(self, args: list = []) -> MesonConfigure:
        return self._configure.run(args=args)

    def setup(self, args: list = []) -> MesonSetup:
        return self._setup.run(args=args)

    def subprojects(self) -> MesonSubprojects:
        return self._subprojects

    def compile(self, args: list = []) -> MesonCompile:
        return self._compile.run(args=args)

    def install(self, args: list = []) -> MesonInstall:
        return self._install.run(args=args)

    def build(self) -> MesonBuild:
        return self._build.run()

    def clean(self) -> MesonClean:
        return self._clean.run()

    def init(self, args: list = []) -> MesonInit:
        return self._init.run(args=args)

    def dist(self, args: list = []) -> MesonDist:
        return self._dist.run(args=args)

    def test(self) -> MesonTest:
        return self._test.run()

    def wrap(self) -> MesonWrap:
        return self._wrap
