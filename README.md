cgaljs
======

This is a project to aid porting [CGAL](http://www.cgal.org/) code to Javascript using an amazing tool called [Emscripten](https://github.com/kripken/emscripten) 

It includes an Emscripten build for [GMP](http://gmplib.org/) and [MPFR](http://www.mpfr.org/) (dependencies of CGAL), which may be of use in their own right.

Dependencies
------------

* Emscripten (and all its requirements including Python, Clang, Java, and NodeJS)
* Emscripten tools must be on the path
* Linux build tools
 
To get started
--------------

* Clone the Git repo
* Run the build_all.py script
* You should find the generated libs in the libs dir, and includes for each dependency in the includes dir
* In examples there's a simple test script you can run to demontrate the output running in NodeJS

Issues & Limitations
--------------------

* This is only the CGAL core. The QT visualisation components have not been done.
* There is no way to tell Javascript how to round floating point ops, so currently non-simple CGAL kernels will likely produce assertion errors (hence the need to patch FPU.h) 
* It is *not* a Javascript library - only a tool to prepare the CGAL library and its dependencies for use with Emscripten
* The dependency on Boost Thread has been removed (for obvious reasons)
* Generated Javascript code is a little large. Experiment with -O2 and -O3 Emscripten optimisation settings)

NB Emscripten Git revision at time of writing:230c0e80dfcd44870bec3254c399db430f6e1d98
