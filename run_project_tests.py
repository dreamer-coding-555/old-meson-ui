#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
import pytest
from mesonui.mesonuilib.utilitylib import OSUtility
from mesonui.mesonuilib.utilitylib import CIUtility
from mesonui.packageinfo import PackageInfo
from mesonui.projectinfo import ProjectInfo
from mesonui.authorinfo import ProjectAuthor
from mesonui.mesonuilib.buildsystem import Meson
import shutil
import logging

logger = logging.getLogger(__name__)
sublogger = logging.getLogger(__name__ + ".log")


class TestPyPiPackageInfo:
    def test_all_pypi_info(self):
        pypi = PackageInfo()
        assert(pypi.get_name() == 'Michael Brockus')
        assert(pypi.get_mail() == 'michaelbrockus@gmail.com')
        assert(pypi.get_license() == 'Apache-2.0')
        assert(pypi.get_project_name() == 'meson-ui')
        assert(pypi.get_version() == '0.20.0')
        assert(pypi.get_description() == 'Meson-UI is a build GUI for Meson build system.')

    def test_only_author_info(self):
        pypi = ProjectAuthor()
        assert(pypi.get_name() == 'Michael Brockus')
        assert(pypi.get_mail() == 'michaelbrockus@gmail.com')

    def test_only_project_info(self):
        pypi = ProjectInfo()
        assert(pypi.get_license() == 'Apache-2.0')
        assert(pypi.get_project_name() == 'meson-ui')
        assert(pypi.get_version() == '0.20.0')
        assert(pypi.get_description() == 'Meson-UI is a build GUI for Meson build system.')


class TestMeson:

    def test_change_sourcedir(self):
        meson = Meson('test/dir/one', 'test/dir/one/builddir')

        assert(meson.sourcedir == 'test/dir/one')
        assert(meson.builddir == 'test/dir/one/builddir')

        meson.sourcedir = 'test/dir/two'
        meson.builddir = 'test/dir/two/builddir'

        assert(meson.sourcedir == 'test/dir/two')
        assert(meson.builddir == 'test/dir/two/builddir')

    def test_setup_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=(tmpdir / 'meson-tmp'), builddir=(tmpdir / 'meson-tmp', 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').ensure()
        assert tmpdir.join('meson-tmp', 'builddir').ensure()

    def test_build_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.build()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_configure_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.configure(['--werror', '--buildtype=minsize'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_rebuild_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        meson.setup(['--wipe'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_compile_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_clean_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()
        meson.clean()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_install_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    def test_mtest_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    @pytest.mark.skipif(not shutil.which('git'), reason='Did not find "git" on this system')
    def test_mdist_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=ninja'])
        meson.compile()

        CIUtility._git_init()
        meson.dist()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()
        assert tmpdir.join('builddir', 'meson-dist', 'test_mdist_command0-0.1.tar.xz').ensure()

    def test_init_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c'])
        meson.setup()
        meson.compile()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()


class TestMesonBackend:

    def test_ninjabackend(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c'])
        meson.setup(['--backend=ninja'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()

    @pytest.mark.skipif(not OSUtility.is_osx(), reason='Skipping because Xcode backend only works on OSX systems')
    def test_xcode_backend(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c', '--type=executable'])
        meson.setup(['--backend=xcode'])
        meson.compile()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()
        assert tmpdir.join('builddir', 'test-prog.xcodeproj', 'project.pbxproj').ensure()

    @pytest.mark.skipif(not OSUtility.is_windows(), reason='Skipping because Visual Studio backend only works on Windows')
    def test_vsbackend(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(sourcedir=tmpdir, builddir=(tmpdir / 'builddir'))

        meson.init(['--language=c'])
        meson.setup(['--backend=vs'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson.build').ensure()
        assert tmpdir.join('builddir', 'build.ninja').ensure()
        assert tmpdir.join('builddir', 'compile_commands.json').ensure()
