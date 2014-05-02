"""Setup for mytest2 XBlock."""

import os
from setuptools import setup


def package_data(pkg, root):
    """Generic function to find package_data for `pkg` under `root`."""
    data = []
    for dirname, _, files in os.walk(os.path.join(pkg, root)):
        for fname in files:
            data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


setup(
    name='mytest2-xblock',
    version='0.1',
    description='mytest2 XBlock',   # TODO: write a better description.
    packages=[
        'mytest2',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'mytest2 = mytest2:XBlockTest2',
        ]
    },
    package_data=package_data("mytest2", "static"),
)