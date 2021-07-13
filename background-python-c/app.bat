@echo off
title App-Output
CALL virtual\scripts\activate.bat
start /b cmd /k python -m Server
start /b cmd /k python -m Output
exit