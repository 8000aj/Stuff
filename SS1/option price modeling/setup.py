import setuptools  # important
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("binomial3.pyx")
)
