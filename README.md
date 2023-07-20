# Python API Automation Framework
# Intregration Test Case For the Restful Booker

URL :https://restful-booker.herokuapp.com/apidoc/index.html

1. GET, POST , PATCH , DELETE , PUT
2. Response Body, Headers , Status Code
3. Auth - Basic Auth , Cookie Base Auth.
4. JSON Schema validation


# Tech Stack (Python Packages used)
1. Request Module 
2. PyTest , PyTest-html
3. Allure Report
4. Faker, CSV , JSON , YAML
5. Run via commandline - Jenkins

# python package manager 
pip install pytest pytest-html faker allure-pytest requests jsonschema

# How to write your report 
pytest  -s -v --alluredir=./reports --html=report.html
# To Create all Requirement document
pip install requirements.txt

# How to Run via Jenkins?

