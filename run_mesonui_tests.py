#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.view.main_activity import MainActivity
from mesonui.view.setup_activity import SetupActivity
from mesonui.view.conf_activity import ConfigureActivity
from mesonui.models.appmodel import MainModel
from mesonui.mesonuilib.buildsystem import Meson
from PyQt5.QtCore import Qt
from pathlib import Path
from os.path import join as join_paths
import os


class TestMainActivity:
    def test_build_prog(self, qtbot):
        main_view: MainActivity = MainActivity(model=MainModel())

        main_view.project_sourcedir.clear()
        main_view.project_builddir.clear()
        qtbot.keyClicks(main_view.project_sourcedir, str(Path(join_paths('test-cases', 'meson-ui', '01-build-prog')).resolve()))
        qtbot.keyClicks(main_view.project_builddir, str(Path(join_paths('test-cases', 'meson-ui', '01-build-prog', 'builddir')).resolve()))

        assert main_view.get_sourcedir() == str(Path(join_paths('test-cases', 'meson-ui', '01-build-prog')).resolve())
        assert main_view.get_builddir() == str(Path(join_paths('test-cases', 'meson-ui', '01-build-prog', 'builddir')).resolve())

        qtbot.addWidget(main_view)
        meson = Meson(main_view.get_sourcedir(), main_view.get_builddir())
        meson.setup()

        qtbot.mouseClick(main_view.control_push_build, Qt.LeftButton)

    def test_build_prog_with_tests(self, qtbot):
        main_view: MainActivity = MainActivity(model=MainModel())

        main_view.project_sourcedir.clear()
        main_view.project_builddir.clear()
        qtbot.keyClicks(main_view.project_sourcedir, str(Path(join_paths('test-cases', 'meson-ui', '02-test-prog')).resolve()))
        qtbot.keyClicks(main_view.project_builddir, str(Path(join_paths('test-cases', 'meson-ui', '02-test-prog', 'builddir')).resolve()))

        assert main_view.get_sourcedir() == str(Path(join_paths('test-cases', 'meson-ui', '02-test-prog')).resolve())
        assert main_view.get_builddir() == str(Path(join_paths('test-cases', 'meson-ui', '02-test-prog', 'builddir')).resolve())

        qtbot.addWidget(main_view)
        meson = Meson(main_view.get_sourcedir(), main_view.get_builddir())
        meson.setup()

        qtbot.mouseClick(main_view.control_push_build, Qt.LeftButton)
        qtbot.mouseClick(main_view.control_push_test, Qt.LeftButton)


class TestSetupActivity:
    def test_do_setup_prog(self, qtbot):
        model: MainModel = MainModel()
        model.model_project().set_sourcedir(Path(join_paths('test-cases', 'meson-ui', '03-setup')).resolve())
        model.model_project().set_builddir(Path(join_paths('test-cases', 'meson-ui', '03-setup', 'builddir')).resolve())
        setup_view: SetupActivity = SetupActivity(None, model)
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_do_setup, Qt.LeftButton)

    def test_no_setup_prog(self, qtbot):
        setup_view: SetupActivity = SetupActivity(None, MainModel())
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_no_setup, Qt.LeftButton)


class TestConfigureActivity:
    def test_do_configure_prog(self, qtbot):
        model: MainModel = MainModel()
        model.model_project().set_sourcedir(Path(join_paths('test-cases', 'meson-ui', '03-setup')).resolve())
        model.model_project().set_builddir(Path(join_paths('test-cases', 'meson-ui', '03-setup', 'builddir')).resolve())
        setup_view: ConfigureActivity = ConfigureActivity(None, model)
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_do_setup, Qt.LeftButton)

    def test_no_configure_prog(self, qtbot):
        setup_view: ConfigureActivity = ConfigureActivity(None, MainModel())
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_no_setup, Qt.LeftButton)
