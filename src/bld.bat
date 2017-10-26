setlocal EnableDelayedExpansion

cd %~dp0src/cpp
if errorlevel 1 exit 1

cmake -G "NMake Makefiles" ^
      -DCMAKE_BUILD_TYPE:STRING=Release ^
      -DCMAKE_PREFIX_PATH:PATH="%LIBRARY_PREFIX%" ^
	  .
	  
if errorlevel 1 exit 1

nmake
if errorlevel 1 exit 1

move mesh_polyhedral_domain.exe %~dp0src/tetmesh
if errorlevel 1 exit 1
cd %~dp0src
if errorlevel 1 exit 1

%PYTHON% setup.py install
if errorlevel 1 exit 1
