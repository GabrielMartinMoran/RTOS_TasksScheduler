import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "str_untref_2020",
    version = "0.0.1",
    author = "Gabriel Moran, Oscar Argueyo",
    author_email = "MORAN.GABRIEL.95@gmail.com, oaargueyo@gmail.com",
    description = ("Trabajo practico final de un sistema en tiempo real "),
    license = "BSD",
    keywords = "UNTREF STR",
    url = "https://gitlab.com/str-untref/tp-finaL",
    packages=['src', 'test'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 0 - Alpha",
        "Topic :: Project",
        "License :: OSI Approved :: BSD License",
    ],
)