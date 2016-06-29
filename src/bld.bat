set CMAKE_PREFIX_PATH=%LIBRARY_PREFIX%
cd %~dp0cpp
if errorlevel 1 exit 1

cmake -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX="%LIBRARY_PREFIX%" -G"NMake Makefiles" .
if errorlevel 1 exit 1

nmake
if errorlevel 1 exit 1
nmake install
if errorlevel 1 exit 1

move mesh_polyhedral_domain.exe %~dp0
if errorlevel 1 exit 1
cd %~dp0
if errorlevel 1 exit 1

%PYTHON% setup.py install
if errorlevel 1 exit 1