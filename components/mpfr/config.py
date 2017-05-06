NAME = 'mpfr'
VERSION = '3.1.1'
DOWNLOADS = ['http://www.mpfr.org/mpfr-%s/mpfr-%s.tar.bz2' % (VERSION,VERSION)]
SOURCE_DIR = 'mpfr-%s' % VERSION
CONFIGURE_CMD = 'EMCONFIGURE_JS=1 emconfigure ./configure --with-gmp-include={includes}/gmp --with-gmp-lib={libs}'
MAKE_CMD = 'emmake make -j4'
CONFIG_PATCHES = [
    {
        'file': 'configure',
        'patch': 'configure.patch'
    }
]
ARTIFACTS =  {
    'includes': [{
                     'source':'mpfr-%s/src' % VERSION,
                     'name':'mpfr'
                 }],
    'libs': [{
                 'source': 'mpfr-%s/src/.libs/libmpfr.so' % VERSION,
                 'name':'libmpfr.so'
             }]
}





