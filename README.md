# SnapToCode 


A FastAPI application that generates code from input files.

 Table of Contents 
- [Introduction](#introduction)
- [Features](#features) 
- [Requirements](#requirements) 
- [Installation](#installation) 
- [Usage](#usage) 
- [Contributing](#contributing)  
- [API Documentation](#api-documentation) 
 

## Introduction 
SnapToCode is a FastAPI application that generates code from input files. It takes in a directory of input files and generates corresponding code files in a specified output directory.

## Features 
Generates code from input files Supports multiple input file formats Customizable output file format Fast and efficient code generation Requirements Python 3.11+ FastAPI Docker Installation To install the application, follow these steps:

## Requirements
Python 3.11+ FastAPI
Langchain Groq
PaddleOCR
PaddlePaddle

## Installation
Clone the repository: git clone https://github.com/your-username/snap-to-code.git Change into the repository directory: cd snap-to-code
Generate Groq API Key from https://console.groq.com/keys
Create .env file in the root directory
Add GROQ_API_KEY in .env with the key generated.
Run the application: uvicorn main:app --reload
Add the project Path as Path where images are saved.
Add output Path as path where project is to be created.

Note: Currently The application will create on ly the files which are of .py
Input images should be .jpg format only. No other format is supported.

Sample project path
./Project_name/src/module1/1.jpg
./Project_name/src/module1/2.jpg
./Project_name/src/module1/3.jpg
./Project_name/src/module2/1.jpg
./Project_name/src/module2/2.jpg

Project structure to be created:
./Project_name/src/module1.py
./Project_name/src/module2.py

.__init__.py file will be created in each folder.



Open a web browser and navigate to http://localhost:8000 Click on the "Generate Code" button Select the input file directory and output file directory Click on the "Generate" button to generate the code API Documentation The API documentation is available at http://localhost:8000/docs

## Contribution
Contributing Contributions are welcome! To contribute, follow these steps:

Fork the repository: git fork https://github.com/your-username/snap-to-code.git Make changes to the code Commit the changes: git commit -m "your commit message" Push the changes to your fork: git push origin your-branch Create a pull request to merge the changes into the main repository License The application is licensed under the MIT License. See the LICENSE file for details.

Note: This is just a sample content, you should adjust it according to your project's specific needs and features.