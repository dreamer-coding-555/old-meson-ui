# Meson Documentation

## Build dependencies

Meson-UI uses Meson and [hotdoc](https://github.com/hotdoc/hotdoc) for generating documentation.

Minimum required version of hotdoc is *0.8.9*.

Instructions on how to install hotdoc are [here](https://hotdoc.github.io/installing.html).

## Building the documentation

From the Meson-UI repository root dir:
```
$ cd docs/
$ meson built_docs
$ ninja -C built_docs/
```
Now you should be able to open the documentation locally
```
built_docs/Meson-UI documentation-doc/html/index.html
```

## Upload

Meson-UI uses the git-upload hotdoc plugin which basically
removes the html pages and replaces with the new content.

You can simply run:
```
$ ninja -C built_docs/ upload
```

## Contributing to the documentation

Commits that only change documentation should have `[skip ci]` in their commit message, so CI is not run (it is quite slow).
For example:
```
A commit message [skip ci]
```
