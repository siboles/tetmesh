set CMAKE_PREFIX_PATH=%LIBRARY_PREFIX%

cd %~dp0src/cpp

cmake -DCMAKE_BUILD_TYPE=Release -G"NMake Makefiles" -DCMAKE_CXX_COMPILER="C:\Program Files (x86)\Microsoft Visual Studio 14.0\VC\bin\nmake.exe"
if errorlevel 1 exit 1

nmake
if errorlevel 1 exit 1
move mesh_polyhedral_domain.exe %~dp0 

cd %~dp0

%PYTHON% setup.py install
