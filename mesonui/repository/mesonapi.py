#!/usr/bin/env python3
#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
from ..mesonuilib.utilitylib import MesonUiException
from .datascanner import MesonScriptReader
from .datareader import MesonBuilddirReader
from .dataloader import MesonBuilddirLoader
from os.path import join as join_paths
from pathlib import Path
import os


class MesonAPI:
    def __init__(self, sourcedir: Path = None, builddir: Path = None):
        super().__init__()
        self._sourcedir: Path = sourcedir
        self._builddir: Path = builddir
        self._builddir_reader = MesonBuilddirReader(self._builddir)
        self._builddir_loader = MesonBuilddirLoader(self._builddir)
        self._script_scanner = MesonScriptReader(self._sourcedir)

    def get_object(self, group: str = None, extract_method: str = 'script', use_fallback: bool = False) -> any:
        if extract_method == 'reader':
            if use_fallback is False and os.path(join_paths(str(self._builddir), 'build.ninja')).exists():
                return self._builddir_reader.extract_from(group=group)
            elif use_fallback is True or Path().joinpath(str(self._sourcedir), 'meson.build').exists():
                return self._script_scanner.extract_from(group=group)
            else:
                return None

        elif extract_method == 'loader':
            if use_fallback is False and os.path(join_paths(str(self._builddir), 'build.ninja')).exists():
                return self._builddir_loader.extract_from(group=group)
            elif use_fallback is True or Path().joinpath(str(self._sourcedir), 'meson.build').exists():
                return self._script_scanner.extract_from(group=group)
            else:
                return None

        elif extract_method == 'script':
            if Path().joinpath(str(self._sourcedir), 'meson.build').exists():
                return self._script_scanner.extract_from(group=group)
            else:
                return None
        else:
            raise MesonUiException(f'Extract method {extract_method} not found in Meson "JSON" API!')
