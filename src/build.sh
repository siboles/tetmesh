#!/bin/sh
cd src/cpp
cgal_create_CMakeLists -s mesh_polyhedral_domain
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_COMPILER=/opt/conda/bin/gcc .
make
mv mesh_polyhedral_domain ../tetmesh/
cd ..
$PYTHON setup.py install --single-version-externally-managed --record=record.txt

