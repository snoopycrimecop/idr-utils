"""\
Tools for managing IDR data.
"""

from setuptools import setup


NAME = "idr-utils"
DESCRIPTION = __doc__
URL = "https://github.com/IDR/idr-utils"
CLASSIFIERS = [
    "Programming Language :: Python",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
    "Intended Audience :: Science/Research",
]


setup(
    name=NAME,
    description=DESCRIPTION,
    url=URL,
    version="0.1.dev",
    classifiers=CLASSIFIERS,
    packages=["pyidr"],
    install_requires=[
        "PyYAML",
        "pandas<0.19",
        "flake8",
        "yamllint"
    ]
)
