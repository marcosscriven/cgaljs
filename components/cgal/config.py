NAME = 'cgal'
VERSION = '4.1'
# Unfortunately there's no way to generate the URL based on version. Only the ID in the URL below is actually used
DOWNLOADS = ['https://gforge.inria.fr/frs/download.php/31640/CGAL-4.1.tar.bz2']
SOURCE_DIR = 'CGAL-%s' % VERSION
SOURCE_PATCHES = [
    {'file': 'cmake/modules/CGAL_SetupBoost.cmake', 'patch': 'CGAL_SetupBoost.cmake.patch'},
    {'file': 'include/CGAL/config.h', 'patch': 'config.h.patch'},
    {'file': 'include/CGAL/FPU.h', 'patch': 'FPU.h.patch'},
    {'file': 'include/CGAL/Interval_nt.h', 'patch': 'Interval_nt.h.patch'},
    {'file': 'CMakeLists.txt', 'patch': 'CMakeLists.txt.patch'},
    ]
CONFIGURE_CMD = ' '.join([
    'cmake',
    '-DGMP_INCLUDE_DIR:STRING={includes}/gmp',
    '-DGMP_LIBRARIES:STRING={libs}/libgmp.so',
    '-DMPFR_INCLUDE_DIR:STRING={includes}/mpfr',
    '-DMPFR_LIBRARIES:STRING={libs}/libmpfr.so',
    '-DWITH_CGAL_ImageIO=OFF',
    '-DWITH_CGAL_Qt3:BOOL=OFF',
    '-DWITH_CGAL_Qt4:BOOL=OFF',
    '-DBoost_INCLUDE_DIRS:STRING={includes}',
    '-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON',
    '-DCMAKE_TOOLCHAIN_FILE={component_dir}/cmake-emcc-toolchain.txt',
    '-DCMAKE_BUILD_TYPE=Release',
    '-DCMAKE_CXX_FLAGS="-v -U__SSE2_MATH__ --ignore-dynamic-linking -DCGAL_HAS_NO_THREADS -U__GNUG__ -DCGAL_NO_ASSERTIONS -DCGAL_FORWARD -DBOOST_MATH_DISABLE_STD_FPCLASSIFY -DBOOST_NO_NATIVE_LONG_DOUBLE_FP_CLASSIFY -DBOOST_MATH_NO_LONG_DOUBLE_MATH_FUNCTIONS"'
])
MAKE_CMD = 'emmake make -j4'
ARTIFACTS =  {
    'includes': [
        {'source':'CGAL-%s/include/' % VERSION, 'name':'cgal'}
    ],
    'libs': [
        {'source': 'CGAL-%s/lib/libCGAL.so' % VERSION,'name':'libcgal.so'},
        {'source': 'CGAL-%s/lib/libCGAL_Core.so' % VERSION,'name':'libcgal_core.so'},
    ]
}
