#!/bin/sh
cd src/cpp
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_COMPILER=/opt/conda/bin/gcc .
make
mv mesh_polyhedral_domain ../tetmesh/
cd ..
$PYTHON setup.py install --single-version-externally-managed --record=record.txt

