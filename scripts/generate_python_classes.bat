@echo off
rem Ensure that you are in the project root directory
python scripts/generate_classes.py
python -m datamodel_code_generator --input schemas/json --output backend/horizon_ui/models --input-file-type jsonschema
echo Python classes generated successfully.