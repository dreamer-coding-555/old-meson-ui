## fixed buildtype optimizations

When using either `-Dbuildtype` or `-Doptimization + -Ddebug`. When both it is redundant
since they override each other. See: https://mesonbuild.com/Builtin-options.html#build-type-options.

Both `optimization` and `debug` are removed, to simplify things.
