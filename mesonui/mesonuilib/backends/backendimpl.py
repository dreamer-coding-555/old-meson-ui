#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#


class BackendImpl:
    def __init__(self, meson_api):
        self._meson_api = meson_api

    def generator(self):
        raise NotImplementedError('Backend "generator" method not implmented!')

    @property
    def projectinfo(self):
        return self._meson_api.get_object(group='projectinfo', extract_method='loader')

    @property
    def targetsinfo(self):
        return self._meson_api.get_object(group='targets', extract_method='loader')

    @property
    def mesoninfo(self):
        return self._meson_api.get_object(group='meson-info', extract_method='loader')

    @property
    def testinfo(self):
        return self._meson_api.get_object(group='tests', extract_method='loader')

    @property
    def buildfiles(self):
        return self._meson_api.get_object(group='buildsystem-files', extract_method='loader')

    @property
    def buildoptions(self):
        return self._meson_api.get_object(group='buildoptions', extract_method='loader')
