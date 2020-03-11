---
short-description: Simplest tutorial
...

# Tutorial

This page shows from the ground up how to create a Meson build
project from Meson-UI.

The humble beginning
-----

Meson is different from some other build systems in that it
does not permit in-source builds. You must always create a separate build directory.
Common convention is to put the default build directory in a subdirectory of your
top level source directory.

First enter the paths for `sourcedir` and `builddir` directory to your Meson
project or click on `open sourcedir` and use the directory pickture to set
`sourcedir` value.

![tutorial](images/tutorial-1.png)


To make it easier for new developers to start working, Meson ships
a tool to generate the basic setup of different kinds of projects.
This functionality can be accessed with the `init project` command. A
typical project setup would go like this:

![tutorial](images/tutorial-2.png)


In my example I left the defualt values. We are now ready to build our application.
First we need to initialize the build by opening `setup project` dialog.

![tutorial](images/tutorial-3.png)


To build our application. We click `build project`.

![tutorial](images/tutorial-4.png)

And assuming you navigated to your project root directory you 
can run the resulting binary from the command line.

```console
$ ./builddir/demo
```

This produces the expected output.

```console
    This is project demo.
```
