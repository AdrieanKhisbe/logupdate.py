#!/usr/bin/env python

from setuptools import setup

setup(
    name="logupdate",
    version="0.2.1",
    author="Adriean Khisbe",
    author_email="adriean.khisbe@live.fr",
    description="Log by overwriting the previous output in the terminal",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://github.com/AdrieanKhisbe/logupdate.py",
    license="MIT",
    packages=["logupdate"],
    install_requires=["cursor", "ansiwrap"],
    # TODO setup tests
    # tests_require=["tox", "pytest", "ansicolors>=1.1.8", "coverage", "pytest-cov"],
    # test_suite="test",
    keywords="", # TODO
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Logging"
        ]
)
