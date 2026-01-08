from setuptools import setup, Extension
from Cython.Build import cythonize

extensions = [
    Extension(
        name="lpunpack",                 # NAMA MODULE (PENTING)
        sources=["src/lpunpack_src.pyx"] # PATH SOURCE
    )
]

setup(
    ext_modules=cythonize(
        extensions,
        compiler_directives={
            "language_level": "3",
            "boundscheck": False,
            "wraparound": False,
            "initializedcheck": False,
        }
    )
)
