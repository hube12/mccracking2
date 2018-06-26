from distutils.core import setup
from Cython.Build import cythonize
import numpy
setup(
    name = "genlayer",
    ext_modules = cythonize('*.py', include_path = [numpy.get_include()]),

)