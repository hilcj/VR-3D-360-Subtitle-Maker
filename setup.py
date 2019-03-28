from glob import glob
from setuptools import setup
from Cython.Build import cythonize

setup(
  name="cythons",
  scripts=glob("*"),
  ext_modules=cythonize("*.pyx")
)