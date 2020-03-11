#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from mesonui.view.main_activity import MainActivity
from mesonui.models.appmodel import MainModel


#
# TODO: need to write more test for UI
class TestMainActivity:
    def test_app(self, qtbot):
        main_view: MainActivity = MainActivity(model=MainModel())
        qtbot.addWidget(main_view)
