=========================================================================
              RiffRipper - Readme & Usage Guide
=========================================================================

RiffRipper - Automatic Archive Extraction Tool
Version: 1.0
Author: NplusM
Last Updated: August 23, 2023
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Introduction:
RiffRipper is a Python-based utility that automates the extraction of compressed music files. It provides a graphical user interface to select source and extraction folders and offers various options for customizing the extraction process.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features:

Directory-Based Extraction: Easily extract all the compressed files from a specific directory.

Various File Types: Supports extraction of .zip, .rar, .7z, etc., via different extraction methods.

Logging: Records all actions performed during extraction, including success and errors.

Delete After Extraction: Option to delete the compressed files after successful extraction.

Multithreading: Speed up the extraction process by enabling multithreading.

Choose Extractor: Choose between built-in Python or 7-zip methods for extraction.

Duplication Check: Checks for existing files by the same name before extracting to prevent duplicate extractions.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation:
To install RiffRipper, follow the steps below.

Prerequisites:
Python 3.7 or higher installed on your machine
pip installed (Python package installer)
Steps
Clone the Repository:

bash
Copy code
git clone https://github.com/NplusM420/RiffRipper.git

Navigate to Project Directory:

bash
Copy code
cd RiffRipper
Create a Virtual Environment (Optional but Recommended):

bash
Copy code
python -m venv venv
Activate the Virtual Environment:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Windows:

bash
Copy code
.\venv\Scripts\activate
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

MacOS/Linux:
bash
Copy code
source venv/bin/activate
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Activate Virtual Environment:

If you created a virtual environment during installation, make sure to activate it before running the application.

Run the Application:

bash
Copy code
python main.py
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Configure Settings:

Source Directory: The folder containing your compressed music files.

Extraction Path: The folder where the extracted files will be saved.

Delete After Extraction: Toggle this to delete the compressed file after successful extraction.

Extractor Type: Choose the type of extraction method ("Python" or "7-zip").

Multithreading: Enable or disable multithreading for faster extraction.

Start the Extraction:

Click on the Extract button to start the extraction process. The progress will be logged and displayed.
=========================================================================
Thank you for using the RiffRipper Tool! For any issues or feedback, please refer to the original script developer.
=========================================================================

**NOTE: This tool has only been tested on Windows, Mac/Linux users should be able to use this but may face unknown issues.