cmake_minimum_required(VERSION 3.16.3 FATAL_ERROR)

project(test-prog)

include(CTest)

add_executable(main_exe "main.cc")
add_test(NAME "test_exe" COMMAND "main_exe")
