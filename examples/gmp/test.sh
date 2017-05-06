emcc test.c -I ../../includes/gmp ../../libs/libgmp.so -o test.js
nodejs test.js 2000
