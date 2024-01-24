set OSGEO4W_ROOT=C:\OSGeo4W
set GDAL_DATA=C:\Program Files\QGIS 3.22.1\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v
Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v
GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v
PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"

