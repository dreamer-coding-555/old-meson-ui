## removed build options `b_asneeded` and `b_bitcode`

Some build options were incompatible with the `setup` and `configure` build commands.
When `b_asneeded` and `b_bitcode` is used in tyhe same command as a "warning" 
printed, it stopped the build.

https://mesonbuild.com/Builtin-options.html#notes-about-apple-bitcode-support

Both had to be removed.
