project('subprog', 'cpp',
    meson_version: '>=0.53.0',
    default_options: ['layout=flat', 'werror=true', 'cpp_std=c++17'])


unittest_cpp_dep = dependency('unittest-cpp', fallback: ['unittest-cpp', 'unittest_cpp_dep'])

exe = executable('prog', 'main.cc', dependencies: [unittest_cpp_dep])

test('run test on exe', exe)
