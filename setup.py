from distutils.core import setup
from Cython.Build import cythonize

setup(name="urlparse",
      ext_modules=cythonize('urlparse.py'))  # Change to .pyx when we have one