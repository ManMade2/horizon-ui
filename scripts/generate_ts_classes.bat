@echo off
REM Ensure that you are in the project root directory

rem Set the path to the directory you want to delete files from
set "directory=%~dp0../frontend/src/models"

rem Check if the directory exists
if not exist "%directory%" (
    echo The directory "%directory%" does not exist.
    exit /b 1
)

rem Delete all files in the directory
del /Q "%directory%\*.*"

PowerShell -Command "Get-ChildItem -Path schemas\*.avsc | ForEach-Object { npx @ovotech/avro-ts-cli $_.FullName -O frontend/src/models }"
echo TypeScript classes generated successfully.
