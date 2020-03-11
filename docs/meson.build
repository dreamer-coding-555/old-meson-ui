#  author : Michael Brockus.  
#  contact: <mailto:michaelbrockus@gmail.com>
#  license: Apache 2.0 :http://www.apache.org/licenses/LICENSE-2.0
#
#  copyright 2020 The Meson-UI development team
#
project('Meson-UI documentation', version: '1.0')

#
# here we import the HotDoc module from
# Meson build standard library.
hotdoc = import('hotdoc')

#
# here we create are hotdoc object, adding
# any info needed to create the docs.
docs = hotdoc.generate_doc(meson.project_name(),
    project_version: meson.project_version(),
    sitemap: 'sitemap.txt',
    build_by_default: true,
    index: 'markdown/index.md',
    install: false,
    extra_assets: ['images/'],
    include_paths: ['markdown'],
    default_license: 'CC-BY-SAv4.0',
    html_extra_theme: join_paths('theme', 'extra'),
    git_upload_repository: 'git@github.com:michaelbadcrumble/meson-ui.github.io.git',
    edit_on_github_repository: 'https://github.com/michaelbadcrumble/meson-ui/',
    syntax_highlighting_activate: true,
)

#
# here we add a command for uploading docs to
# Meson-UI project's home page hosted on GitHub.
run_target('upload',
    command: [find_program('hotdoc'), 'run', '--conf-file', docs.config_path()]
)
