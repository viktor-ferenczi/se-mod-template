@echo off

IF EXIST "%AppData%\SpaceEngineers\Mods" GOTO Skip1
mkdir "%AppData%\SpaceEngineers\Mods" 2>&1 >NUL
:Skip1

IF EXIST "%AppData%\SpaceEngineers\Mods\ModTemplate" GOTO Skip2 
mklink /J "%AppData%\SpaceEngineers\Mods\ModTemplate" "%1\Mod"
:Skip2

echo Done
