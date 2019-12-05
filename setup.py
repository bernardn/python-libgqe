#!/usr/bin/env python3

import sys
try:
    from setuptools import setup, find_packages
    # from setuptools.command.build_py import build_py
    # from setuptools.command.install_lib import install_lib as InstallLib
    # from setuptools.command.install_scripts import install_scripts as InstallScripts
except ImportError:
    print("The 'setuptools' python library is needed for LibGQE to build.", file=sys.stderr)
    sys.exit(1)

version = None

try:
    with open('VERSION') as version_file:
        version = version_file.read().strip()

except FileNotFoundError:
    print("VERSION file not found. It must contain the current software revision as the sole string.", file=sys.stderr)


setup(
    name='libgqe',
    version='0.0.1',
    packages=[
        "libgqe",
        "libgqe.format",
        "libgqe.protocol",
        "libgqe.protocol.GQRFC1201",
        "libgqe.protocol.GQRFC1201.v1_40",
        "libgqe.protocol.GQRFC1701",
        "libgqe.protocol.GQRFC1701.v1_00",
        "libgqe.protocol.GQRFC1701.v2_00",
        "libgqe.protocol.GQRFC1701.v2_01",
        "libgqe.protocol.GQRFC1801",
        "libgqe.protocol.GQRFC1801.v1_00",
        "libgqe.unit",
        "libgqe.unit.gmc",
        "libgqe.unit.gmc.re_1_00",
        "libgqe.unit.gqemf",
        "libgqe.unit.gqemf.re_1_00",
        "libgqe.unit.gqemf.re_2_00",
        "libgqe.unit.gqemf.re_2_16",
    ],
    scripts=['gqe-cli'],
    url='https://github.com/bernardn',
    license='GPL v2',
    author='Bernard Nauwelaerts',
    author_email='',
    description='A library for interfacing device units made by GQ Electronics LLC',
    python_requires='>=3.5',
)
