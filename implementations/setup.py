from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize("replace_color.pyx")
)

setup(
    ext_modules = cythonize("create_vr_mapping.pyx")
)

setup(
    ext_modules = cythonize("alpha_blend.pyx")
)