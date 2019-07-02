@echo off
set this_path=%~dp0
set env_path=%PATH%;%~dp0

set var=
:loop
set /p var="Set Environment Path (y/n)?: "
if "%var%"=="y" goto env
if "%var%"=="n" goto setting
echo '%var%' was not in expected response: y, n
goto loop


:env
set p=%PATH%

:envl
for /f "tokens=1* delims=;" %%a in ("%p%") do (
	if "%%a"=="%this_path%" goto setting
	set p=%%b
)
if defined p goto envl
setx /m PATH "%env_path%


:setting
if exist %LOCALAPPDATA%\mcdp goto setting2
md %LOCALAPPDATA%\mcdp

:setting2
@echo [Path]>%LOCALAPPDATA%\mcdp\mcdp_config.ini
@echo Install=%this_path%>>%LOCALAPPDATA%\mcdp\mcdp_config.ini


:end
echo Installed successfully!
pause