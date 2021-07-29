@echo off

setlocal ENABLEDELAYEDEXPANSION

if "%1" == "" goto usage
if "%1" == "-run" goto run
if "%1" == "-time" goto time


rem --- call ourselves using extended cmd mode
cmd /V:ON /C %0 -run %1
goto end

:run

rem --- generate unique filename
set host=%2
set filename=%host%

for /F "tokens=2,3,4,5,6,7 delims=:./ " %%a  in ("%date% %time%") do set filename=!filename!_%%c_%%a_%%b__%%d_%%e_%%f_ping.log

echo %filename%

rem ---we want to have 1 file for ~1 hr, each 60 pings (~1 min) are interleaved with date/time

for /L %%i in (1, 1, 60) do (
   echo ----------- >> %filename%
   call %0 -time %filename%
   echo ----------- >> %filename%
   ping -n 60 %host% >> %filename%
)

goto run

:time
echo %date% %time% >>%2

goto end

:usage
echo Usage: smartping {hostname}

:end

endlocal
