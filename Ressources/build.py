from distutils.core import setup
from Cython.Build import cythonize
import numpy
setup(
    name = "genlayer",
    ext_modules = cythonize('*.pyx', include_path = [numpy.get_include()]),

)