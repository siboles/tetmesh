from setuptools import setup, find_packages
from setuptools.dist import Distribution
import os
import sys

class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

if os.name == "posix":
    package_data = {"tetmesh": ["*.so", "mesh_polyhedral_domain"]}
elif os.name == "nt":
    print "This"
    package_data = {"tetmesh": ["*.a", "*.exe"]}

setup(
    name = "tetmesh",
    version = "0.0",
    packages = find_packages(),
    package_dir={"tetmesh": "tetmesh"},
    include_package_data=True,
    package_data=package_data,
    distclass=BinaryDistribution,
    author="Scott Sibole",
    author_email="scott.sibole@gmail.com",
    license="GPL",
    install_requires=["trimesh"],
    description="Module wraps an executable for generating tetrahedral meshes using CGAL")
