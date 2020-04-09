---
short-description: Backend reference
...

# Built-in options

Meson has exporters for Visual Studio and XCode, but writing a custom backend for every IDE out there is not a scalable approach. To solve this problem, Meson provides an API that makes it easy for any IDE or build tools to integrate Meson builds and provide an experience comparable to a solution native to the IDE.

Meson-ui tacks advantage of the Meson build systems introspection API for custom
backends such as QtCreator, KDevelop and more.


### Backend table

| Option                               | Supported by  | Description        |
| ------                               | ------------- | ------------------ |
| ninja                                | meson         | Ninja build system |
| xcode                                | meson         | Apple Xcode        |
| vs2010                               | meson         | Visual Studio 2010 |
| vs2015                               | meson         | Visual Studio 2015 |
| vs2017                               | meson         | Visual Studio 2017 |
| vs2019                               | meson         | Visual Studio 2019 |
| qtcreator                            | meson-ui      | QtCreatort IDE     |
| kdevelop                             | meson-ui      | KDevelop IDE       |
| codeblocks                           | meson-ui      | Code::blocks       |
| gnome                                | meson-ui      | GNOME Builder      |
