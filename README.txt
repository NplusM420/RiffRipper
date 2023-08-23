=========================================================================
              RiffRipper - Readme & Usage Guide
=========================================================================

RiffRipper - Automatic Archive Extraction Tool
Version: 1.0
Author: NplusM
Last Updated: August 23, 2023

Introduction:
RiffRipper is a Python script designed to streamline the extraction process for archives (ZIP & RAR files) in a given directory. It uses both Python's built-in zipfile library and the 7-Zip software to handle various archive formats. The tool also comes with features like multithreading for improved extraction speed and an option to delete the original compressed files after successful extraction.

Features:
Automatic Extraction:
Extracts all archives in a specified directory to a target directory.

Multithreading:
Uses multiple threads for faster extraction, reducing the total extraction time. By default, it uses 4 threads. This number can be adjusted for optimal performance.

Error Logging:
Logs any errors encountered during the extraction process for easy troubleshooting.

Optional Deletion:
Provides an option to delete the original archives after successful extraction.

Progress Display:
Utilizes a progress bar to show the ongoing status of the extraction.

Setup & Requirements:
Python:
Ensure that Python (Version 3.6 or above) is installed on your system.

7-Zip:
Install 7-Zip from its official website. Note the path to the 7z.exe executable, as this will be needed for the settings.

settings.json:
This file contains configuration settings for the script. Before running the script, make sure to update settings.json with appropriate values.

source_directory: The directory containing the ZIP & RAR files you wish to extract.
log_location: The path where you want the log file to be saved.
delete_after_extraction: A boolean value (true or false) indicating whether to delete the original archives after extraction.
extractor_type: The type of extractor to use ("python" for zipfile or "7z" for 7-Zip).
7z_path: The path to the 7z executable. Update this if your 7z installation is in a different directory.
Usage:
Update the settings.json file with the appropriate paths and preferences.
Navigate to the directory containing the RiffRipper.py script using a terminal or command prompt.
Run the script using the command python RiffRipper.py.
When prompted, provide the path where you'd like to store your extracted songs. The script will create this directory if it doesn't already exist.
The script will then automatically extract all archives from the source directory to the provided directory, displaying a progress bar.
After extraction, if delete_after_extraction is set to true, the script will ask for confirmation to delete the original archives. Confirm with 'y' to delete or 'n' to retain them.
Support & Troubleshooting:
If the extraction process encounters errors, it will log details about these errors in the specified log file. Check the log file for details on which archives caused problems.

Ensure that the source directory, 7-Zip path, and log locations are correctly specified in the settings.json file.

If you encounter issues related to multithreading or resource usage, you can adjust the MAX_THREADS variable in the RiffRipper.py script to increase or decrease the number of threads used.

=========================================================================
Thank you for using the RiffRipper Tool! For any issues or feedback, please refer to the original script developer.
=========================================================================
