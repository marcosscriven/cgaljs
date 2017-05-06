emcc test.c ../../libs/libmpfr.so ../../libs/libgmp.so -I ../../includes/gmp -I ../../includes/mpfr -o test.js
nodejs test.js
