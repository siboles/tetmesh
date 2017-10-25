#!/bin/sh
cd cpp
echo $PREFIX
cmake -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_PREFIX_PATH=$PREFIX \
      -DCMAKE_INSTALL_PREFIX=$PREFIX \
      -DCMAKE_SYSTEM_PREFIX_PATH=$PREFIX \
      -D BOOST_ROOT=$PREFIX -D Boost_NO_SYSTEM_PATHS=ON \
      -DCMAKE_C_COMPILER=$HOME/anaconda2/bin/gcc .
make
mv mesh_polyhedral_domain ../tetmesh/
cd ..
$PYTHON setup.py install --single-version-externally-managed --record=record.txt

