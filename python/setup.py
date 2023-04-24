#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

requirements = ["floris>=3.0", "openpyxl", "flasc", "jupyter"]

test_requirements = []

setup(
    author="Paul Fleming",
    author_email="paul.fleming@nrel.gov",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="fct_smarteole",
    install_requires=requirements,
    long_description="Collection of modeling and analysis scripts for project 'fct_smarteole'. Heavily relies on FLORIS and FLASC.",
    include_package_data=True,
    keywords="fct_smarteole",
    name="fct_smarteole",
    packages=find_packages(include=["fct_smarteole", "fct_smarteole.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    version="0.1.0",
    zip_safe=False,
)
