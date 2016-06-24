set CMAKE_PREFIX_PATH=%LIBRARY_PREFIX%

cd %~dp0src/cpp

cmake -DCMAKE_BUILD_TYPE=Release -G"NMake Makefiles"
if errorlevel 1 exit 1

nmake
if errorlevel 1 exit 1
move mesh_polyhedral_domain.exe %~dp0 

cd %~dp0

%PYTHON% setup.py install
