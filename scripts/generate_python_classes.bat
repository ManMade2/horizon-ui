@echo off

rem Set the path to the directory you want to delete files from
set "directory=%~dp0../backend/horizon_ui/models"

rem Check if the directory exists
if not exist "%directory%" (
    echo The directory "%directory%" does not exist.
    exit /b 1
)

rem Delete all files in the directory
del /Q "%directory%\*.*"

python scripts/generate_classes.py
rem python -m datamodel_code_generator --input schemas/json --output backend/horizon_ui/models --input-file-type jsonschema
rem python -m datamodel_code_generator --input schemas/json --output backend/horizon_ui/models --input-file-type 
python -m datamodel_code_generator --input schemas/json --output backend/horizon_ui/models --input-file-type openapi

echo Python classes generated successfully.