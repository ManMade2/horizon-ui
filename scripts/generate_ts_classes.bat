@echo off
REM Ensure that you are in the project root directory

PowerShell -Command "Get-ChildItem -Path schemas\*.avsc | ForEach-Object { npx @ovotech/avro-ts-cli $_.FullName -O frontend/src/models }"
echo TypeScript classes generated successfully.
