#!/usr/bin/env python3

#
# author: Michael Brockus
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
import subprocess
import logging

color = {
    'green': '\x1B[01;32m',
    'blue': '\033[94m',
    'bold': '\033[1m',
    'reset': '\x1B[0m'
}

log_format = (
    f'{color["bold"]} cat_log: {color["reset"]}'
    f'{color["blue"]} %(funcName)s - {color["reset"]}'
    f'{color["bold"]} %(levelname)s: {color["reset"]}'
    f'{color["green"]} %(message)s {color["reset"]}'
)

logging.basicConfig(level=logging.INFO, format=log_format)


USER_DEPS: list = [
    'git',
    'ninja',
    'glibc',
    'gcc',
    'gcc-c++',
    'gcc-objc',
    'gcc-obj-c++',
    'gcc-fortran',
    'ldc',
    'rust',
    'java-13-openjdk-devel',
    'mono-core'
]

PYPI_DEPS: list = [
    'meson==0.53.2',
    'cmake==3.16.3',
    'pytest==5.3.2',
    'pytest-cov==2.8.1',
    'codecov==2.0.15',
    'PyQt5==5.14.1'
]


def install_user_packages(deps: list, dry_run: bool = False):
    for dep in deps:
        logging.info(f'installing: {dep}')
        subprocess.check_call([
            'zypper', '--quiet', 'install', '-y', dep])

    for dep in deps:
        logging.info(f'user dep: {dep}')


def install_pypi_packages(deps: list, dry_run: bool = False):
    for dep in deps:
        logging.info(f'installing: {dep}')
        subprocess.check_call([
            'python3', '-m', 'pip', 'install', '--quiet', dep])

    for dep in deps:
        logging.info(f'pypi dep: {dep}')


def main():
    logging.info('Running install commands for both "user" and "python3"')
    install_user_packages(USER_DEPS)
    install_pypi_packages(PYPI_DEPS)
    logging.info('Process done.')


if __name__ == "__main__":
    main()
