@echo off

mkdir "%AppData%\SpaceEngineers\Mods" 2>&1 >NUL
del /f /s /q "%AppData%\SpaceEngineers\Mods\ModTemplate" 2>&1 >NUL
rd /s /q "%AppData%\SpaceEngineers\Mods\ModTemplate" 2>&1 >NUL
mkdir "%AppData%\SpaceEngineers\Mods\ModTemplate" 2>&1 >NUL

xcopy /s /e /y "%1\Mod\" "%AppData%\SpaceEngineers\Mods\ModTemplate\"

echo Done
