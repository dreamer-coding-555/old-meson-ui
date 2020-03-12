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
from mesonui.view.dist_activity import DistActivity
from mesonui.view.init_activity import InitActivity
from mesonui.view.wrap_activity import WrapActivity
from mesonui.view.install_activity import InstallActivity
from mesonui.view.subprojects_activity import SubprojectsActivity
from mesonui.mesonuilib.outputconsole import OutputConsole

from mesonui.models.appmodel import MainModel
from mesonui.mesonuilib.utilitylib import OSUtility
from PyQt5.QtCore import Qt
from os.path import join as join_paths
import pytest


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestMainActivity:
    def test_is_renderable(self, qtbot):
        activity = MainActivity(MainModel())
        qtbot.addWidget(activity)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestSetupActivity:
    def test_is_renderable(self, qtbot):
        activity = SetupActivity(None, MainModel())
        qtbot.addWidget(activity)

    def test_do_setup_prog(self, qtbot):
        model: MainModel = MainModel()
        model.model_project().set_sourcedir(join_paths('test-cases', 'meson-ui', '03-setup'))
        model.model_project().set_builddir(join_paths('test-cases', 'meson-ui', '03-setup', 'builddir'))
        setup_view: SetupActivity = SetupActivity(OutputConsole(MainActivity(MainModel())), model)
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_do_setup, Qt.LeftButton)

    def test_no_setup_prog(self, qtbot):
        setup_view: SetupActivity = SetupActivity(None, MainModel())
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_no_setup, Qt.LeftButton)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestConfigureActivity:
    def test_is_renderable(self, qtbot):
        activity = ConfigureActivity(MainModel())
        qtbot.addWidget(activity)

    def test_do_setup_prog(self, qtbot):
        model: MainModel = MainModel()
        model.model_project().set_sourcedir(join_paths('test-cases', 'meson-ui', '03-setup'))
        model.model_project().set_builddir(join_paths('test-cases', 'meson-ui', '03-setup', 'builddir'))
        setup_view: ConfigureActivity = ConfigureActivity(OutputConsole(MainActivity(MainModel())), model)
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_do_setup, Qt.LeftButton)

    def test_no_setup_prog(self, qtbot):
        setup_view: ConfigureActivity = ConfigureActivity(None, MainModel())
        qtbot.addWidget(setup_view)

        qtbot.mouseClick(setup_view.control_push_no_setup, Qt.LeftButton)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestInitActivity:
    def test_is_renderable(self, qtbot):
        activity = InitActivity(MainModel())
        qtbot.addWidget(activity)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestDistActivity:
    def test_is_renderable(self, qtbot):
        activity = DistActivity(MainModel())
        qtbot.addWidget(activity)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestWrapActivity:
    def test_is_renderable(self, qtbot):
        activity = WrapActivity(MainModel())
        qtbot.addWidget(activity)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestInstallActivity:
    def test_is_renderable(self, qtbot):
        activity = InstallActivity(MainModel())
        qtbot.addWidget(activity)


@pytest.mark.skipif(OSUtility.is_windows() or OSUtility.is_cygwin(), reason='Not sure why but it fails on Windows.')
class TestSubprojectsActivity:
    def test_is_renderable(self, qtbot):
        activity = SubprojectsActivity(MainModel())
        qtbot.addWidget(activity)
