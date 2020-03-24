---
title: Release 0.20.0
short-description: Release notes for 0.20.0
...

# New features

## Run `ninja` versions of commands

Meson-UI now lets you run `ninja` commands in the background.

## New introspection dashboard

Meson-UI now has a dashboard for viewing info from your project.

We currently support project info, build options, and unit tests.

## Support `directory` and `backend` options

Meson-UI now supports options for `directory` and `backend`.

## Support new `meson compile` command

In Meson-UI 0.20.0 a new action was added to support the new `meson compile`
command that was added to Meson 0.54.0 to support backend agnostic compilation.

## Support new `meson init` command

In Meson-UI 0.20.0 a new action was added to support the `meson init`
command so you can generate new sample projects.

## Support `meson subproject` command

In Meson-UI 0.20.0 a new action was added to support the `meson subproject`
command so you can manage your subprojects.

## Fix `meson` build system runners

Fixed issues with Meson-UI build system wrappers not performing
commands in the source root directory.

## Support new `meson wrap` command

In Meson-UI 0.20.0 a new action was added to support the `meson wrap`
command so you can search for wraps, install wrap files, get wrap
info, and more.

## Support new IDE backends

Meson-UI now has backends for `kdevelop`, `codeblocks`, and `qtcreator`.

## Support new `meson configure` command

In Meson-UI 0.20.0 a new action was added to support `meson configure`
command so the user can configure a project after it has been built
from Meson-UI.

