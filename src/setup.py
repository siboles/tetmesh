from setuptools import setup, find_packages
from setuptools.dist import Distribution
import os

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

if os.name == "posix":
    package_data = {"tetmesh": ["linux/*"]}
elif os.name == "nt":
    package_data = {"tetmesh": ["windows/*"]}

setup(
    name = "tetmesh",
    version = "0.0",
    packages = find_packages(),
    include_package_data=True,
    package_data=package_data,
    distclass=BinaryDistribution,
    author="Scott Sibole",
    author_email="scott.sibole@gmail.com",
    license="GPL",
    install_requires=["trimesh"],
    description="Module wraps an executable for generating tetrahedral meshes using CGAL")
