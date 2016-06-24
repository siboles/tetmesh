#!/bin/sh
cd src/cpp
cgal_create_CMakeLists -s executable
cmake -DCMAKE_INSTALL_PREFIX=${PREFIX} -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_C_COMPILER=/opt/conda/bin/gcc .
cd ..
$PYTHON setup.py install --single-version-externally-managed --record=record.txt

