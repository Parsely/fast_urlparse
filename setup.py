from distutils.core import setup
from Cython.Build import cythonize

setup(name="urlparse",
      install_requires=[
            'cython'
      ],
      ext_modules=cythonize('curlparse.pyx'))  # Should be .pyx but can be .py

# To build this...
# python setup.py build_ext --inplace
