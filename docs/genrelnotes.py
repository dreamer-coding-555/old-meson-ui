#!/usr/bin/env python3

#
# author : Michael Brockus.  
# contact: <mailto:michaelbrockus@gmail.com>
# license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
# copyright 2020 The Meson-UI development team
#
import subprocess
import sys
import os
from glob import glob
from os.path import join as join_paths

RELNOTE_TEMPLATE = '''---
title: Release {}
short-description: Release notes for {}
...

# New features

'''

def add_to_sitemap(from_version, to_version):
    '''
       Adds release note entry to sitemap.txt.
    '''
    sitemapfile = join_paths('..', 'sitemap.txt')
    s_f = open(sitemapfile)
    lines = s_f.readlines()
    s_f.close()
    with open(sitemapfile, 'w') as s_f:
        for line in lines:
            if 'Release-notes' in line and from_version in line:
                new_line = line.replace(from_version, to_version)
                s_f.write(new_line)
            s_f.write(line)

def generate(from_version, to_version):
    '''
       Generate notes for Meson-UI build next release.
    '''
    ofilename = f'Release-notes-for-{to_version}.md'
    with open(ofilename, 'w') as ofile:
        ofile.write(RELNOTE_TEMPLATE.format(to_version, to_version))
        for snippetfile in glob(join_paths('snippets', '*.md')):
            snippet = open(snippetfile).read()
            ofile.write(snippet)
            if not snippet.endswith('\n'):
                ofile.write('\n')
            ofile.write('\n')
            subprocess.check_call(['git', 'rm', snippetfile])
    subprocess.check_call(['git', 'add', ofilename])
    add_to_sitemap(from_version, to_version)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(sys.argv[0], 'from_version to_version')
        sys.exit(1)
    FROM_VERSION = sys.argv[1]
    TO_VERSION = sys.argv[2]
    os.chdir('markdown')
    generate(FROM_VERSION, TO_VERSION)
