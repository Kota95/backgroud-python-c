@echo off
title Setup
echo Running Setup...
echo Do not close this Window...
powershell -Command "curl http://download.savannah.gnu.org/releases/tinycc/tcc-0.9.27-win64-bin.zip -O tcc.zip"
powershell Expand-Archive -Path ".\tcc.zip" -DestinationPath ".\\"
DEL /F tcc.zip
python -m venv virtual
CALL virtual\scripts\activate.bat
start pip install -r requirements.txt
exit
