from setuptools import setup
from setuptools.extension import Extension

try:
    import Cython
    USE_CYTHON = True
except:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension("curlparse", ["curlparse" + ext])]

if USE_CYTHON:
    from Cython.Build import cythonize
    extensions = cythonize(extensions)

setup(name='urlparse',
      ext_modules=extensions)

# To build this...
# python setup.py build_ext --inplace
