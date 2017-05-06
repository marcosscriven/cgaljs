#!/usr/bin/python
import os
from tools.build import build_component

INCLUDES_DIR = 'includes'
LIBS_DIR = 'libs'

if not os.path.exists(INCLUDES_DIR):
    os.makedirs(INCLUDES_DIR)

if not os.path.exists(LIBS_DIR):
    os.makedirs(LIBS_DIR)

COMPONENTS = [
    'boost',
    'gmp',
    'mpfr',
    'cgal',
]

for component in COMPONENTS:
    build_component(component, INCLUDES_DIR, LIBS_DIR)


