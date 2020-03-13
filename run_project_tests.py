#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
import pytest
from pathlib import Path
from os.path import join as join_paths
from mesonui.mesonuilib.utilitylib import OSUtility
from mesonui.mesonuilib.utilitylib import CIUtility
from mesonui.packageinfo import PackageInfo
from mesonui.projectinfo import ProjectInfo
from mesonui.authorinfo import ProjectAuthor
from mesonui.mesonuilib.buildsystem import Meson
from mesonui.mesonuilib.buildsystem import CMake
import shutil
import tempfile
import logging

logger = logging.getLogger(__name__)
sublogger = logging.getLogger(__name__ + ".log")

CMAKE_SCRIPT = '''\
cmake_minimum_required(VERSION 3.16.3 FATAL_ERROR)

project(test-prog)

include(CTest)

add_executable(main_exe "main.cc")
add_test(NAME "test_exe" COMMAND "main_exe")

'''

BUILD_SCRIPT = '''\
project('test-prog', 'c', meson_version: '>=0.53.0')

exe = executable('simple-test', ['main.c'])

test('exe test cases', exe)
'''

CPP_SOURCE_FILE = '''\
#include <iostream>

int main()
{
    std::cout << "Basic Test Cases." << std::endl;
    return 0;
}// end of function main

'''

C_SOURCE_FILE = '''\
#include <stdio.h>

int main(void)
{
    puts("Basic Test Cases.");
    return 0;
}// end of function main

'''

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


class TestCMake:

    def test_setup_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        cmake: CMake = CMake(
            sourcedir=(tmpdir / 'cmake-tmp'),
            builddir=(tmpdir / 'cmake-tmp', 'builddir'))

        tmpdir.join('cmake-tmp', 'CMakeLists.txt').write(CMAKE_SCRIPT, ensure=True)
        tmpdir.join('cmake-tmp', 'main.cc').write(CPP_SOURCE_FILE, ensure=True)

        cmake.setup()

        #
        # Run asserts to check it is working
        assert tmpdir.join('cmake-tmp', 'CMakeLists.txt').read() == CMAKE_SCRIPT
        assert (tmpdir / 'cmake-tmp' / 'builddir') == tmpdir.join('cmake-tmp', 'builddir')

    def test_compile_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        cmake: CMake = CMake(
            sourcedir=(tmpdir / 'cmake-tmp'),
            builddir=(tmpdir / 'cmake-tmp', 'builddir'))

        tmpdir.join('cmake-tmp', 'CMakeLists.txt').write(CMAKE_SCRIPT, ensure=True)
        tmpdir.join('cmake-tmp', 'main.cc').write(CPP_SOURCE_FILE, ensure=True)

        cmake.setup()
        cmake.compile()

        #
        # Run asserts to check it is working
        assert tmpdir.join('cmake-tmp', 'CMakeLists.txt').read() == CMAKE_SCRIPT
        assert (tmpdir / 'cmake-tmp' / 'builddir') == tmpdir.join('cmake-tmp', 'builddir')
        assert (tmpdir / 'cmake-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('cmake-tmp', 'builddir', 'build.ninja')

    def test_build_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        cmake: CMake = CMake(
            sourcedir=(tmpdir / 'cmake-tmp'),
            builddir=(tmpdir / 'cmake-tmp', 'builddir'))

        tmpdir.join('cmake-tmp', 'CMakeLists.txt').write(CMAKE_SCRIPT, ensure=True)
        tmpdir.join('cmake-tmp', 'main.cc').write(CPP_SOURCE_FILE, ensure=True)

        cmake.setup()
        cmake.build()

        #
        # Run asserts to check it is working
        assert tmpdir.join('cmake-tmp', 'CMakeLists.txt').read() == CMAKE_SCRIPT
        assert (tmpdir / 'cmake-tmp' / 'builddir') == tmpdir.join('cmake-tmp', 'builddir')
        assert (tmpdir / 'cmake-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('cmake-tmp', 'builddir', 'build.ninja')

    def test_test_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        cmake: CMake = CMake(
            sourcedir=(tmpdir / 'cmake-tmp'),
            builddir=(tmpdir / 'cmake-tmp', 'builddir'))

        tmpdir.join('cmake-tmp', 'CMakeLists.txt').write(CMAKE_SCRIPT, ensure=True)
        tmpdir.join('cmake-tmp', 'main.cc').write(CPP_SOURCE_FILE, ensure=True)

        cmake.setup()
        cmake.build()
        cmake.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('cmake-tmp', 'CMakeLists.txt').read() == CMAKE_SCRIPT
        assert (tmpdir / 'cmake-tmp' / 'builddir') == tmpdir.join('cmake-tmp', 'builddir')

    def test_clean_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        cmake: CMake = CMake(
            sourcedir=(tmpdir / 'cmake-tmp'),
            builddir=(tmpdir / 'cmake-tmp', 'builddir'))

        tmpdir.join('cmake-tmp', 'CMakeLists.txt').write(CMAKE_SCRIPT, ensure=True)
        tmpdir.join('cmake-tmp', 'main.cc').write(CPP_SOURCE_FILE, ensure=True)

        cmake.setup()
        cmake.build()
        cmake.clean()

        #
        # Run asserts to check it is working
        assert tmpdir.join('cmake-tmp', 'CMakeLists.txt').read() == CMAKE_SCRIPT
        assert not (tmpdir / 'cmake-tmp' / 'builddir') == tmpdir.join('cmake-tmp', 'builddir')


class TestMeson:

    def test_setup_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp', 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')

    def test_build_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp', 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.build()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_configure_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.build()
        meson.configure(['--werror', '--buildtype=minsize'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_rebuild_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.build()
        meson.setup(['--wipe'])

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_compile_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.compile()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_clean_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.compile()
        meson.clean()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_mtest_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.build()
        meson.test()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    @pytest.mark.skipif(not shutil.which('git'), reason='Did not find "git" on this system')
    def test_mdist_command(self, tmpdir):
        #
        # Setting up tmp test directory
        with tmpdir.as_cwd():
            pass
        tmpdir.chdir()

        #
        # Running Meson command
        meson: Meson = Meson(
            sourcedir=(tmpdir / 'meson-tmp'),
            builddir=(tmpdir / 'meson-tmp' / 'builddir'))

        tmpdir.join('meson-tmp', 'meson.build').write(BUILD_SCRIPT, ensure=True)
        tmpdir.join('meson-tmp', 'main.c').write(C_SOURCE_FILE, ensure=True)

        meson.setup()
        meson.build()
        CIUtility._git_init((tmpdir / 'meson-tmp'))
        meson.dist()

        #
        # Run asserts to check it is working
        assert tmpdir.join('meson-tmp', 'meson.build').read() == BUILD_SCRIPT
        assert (tmpdir / 'meson-tmp' / 'builddir') == tmpdir.join('meson-tmp', 'builddir')
        assert (tmpdir / 'meson-tmp' / 'builddir' / 'build.ninja') == tmpdir.join('meson-tmp', 'builddir', 'build.ninja')

    def test_init_command(self, tmpdir):
        #
        # Setting up tmp test directory
        for lang in ('c', 'cpp', 'cs', 'java'):
            for target in ('executable', 'library'):
                with tempfile.TemporaryDirectory() as tmp_dir:
                    meson: Meson = Meson(tmp_dir, join_paths(tmp_dir, 'builddir'))
                    meson.init(['--language', lang, '--type', target])
                    meson.setup()
                    meson.compile()

                    #
                    # Run asserts to check it is working
                    assert Path(join_paths(tmp_dir, 'builddir')).is_dir()


class TestMesonBackend:

    def test_ninjabackend(self):
        sourcedir: str = join_paths('test-cases', 'backends', '01-ninjabackend')
        builddir: str = join_paths('test-cases', 'backends', '01-ninjabackend', 'builddir')
        meson = Meson(sourcedir=sourcedir, builddir=builddir)

        meson.setup(args=['--backend=ninja'])
        meson.compile()

        assert(Path(sourcedir).is_dir())
        assert(Path(builddir).is_dir())

    @pytest.mark.skipif(not OSUtility.is_osx(), reason='Skipping because Xcode backend only works on OSX systems')
    def test_xcodebackend(self):
        sourcedir: str = join_paths('test-cases', 'backends', '02-xcodebackend')
        builddir: str = join_paths('test-cases', 'backends', '02-xcodebackend', 'builddir')
        meson = Meson(sourcedir=sourcedir, builddir=builddir)

        meson.setup(args=['--backend=xcode'])
        meson.compile()

        assert(Path(sourcedir).is_dir())
        assert(Path(builddir).is_dir())

    @pytest.mark.skipif(not OSUtility.is_windows(), reason='Skipping because Visual Studio backend only works on Windows')
    def test_vsbackend(self):
        sourcedir: str = join_paths('test-cases', 'backends', '03-vsbackend')
        builddir: str = join_paths('test-cases', 'backends', '03-vsbackend', 'builddir')
        meson = Meson(sourcedir=sourcedir, builddir=builddir)

        meson.setup(args=['--backend=vs'])
        meson.compile()

        assert(Path(sourcedir).is_dir())
        assert(Path(builddir).is_dir())
