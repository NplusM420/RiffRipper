# Riff_Ripper.py
import os
import json
import logging
from zipfile import ZipFile
import subprocess
import concurrent.futures

MAX_THREADS = 4  # You can adjust this value to your liking

def setup_logging(log_location):
    logging.basicConfig(filename=log_location, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def extract_file(entry, settings):
    source_dir = settings["source_directory"]
    extract_dir = settings["extraction_path"]
    extractor_type = settings["extractor_type"]

    if entry.name.endswith('.zip') or entry.name.endswith('.rar'):
        archive_path = os.path.join(source_dir, entry.name)
        
        # Destination folder name is the archive name without extension
        target_folder = os.path.join(extract_dir, os.path.splitext(entry.name)[0])
        
        # If the target folder exists, skip extraction
        if os.path.exists(target_folder):
            logging.info(f"Skipping already extracted archive: {archive_path}")
            return True

        try:
            if extractor_type == "python":
                # Do not attempt to use ZipFile for .rar files
                if entry.name.endswith('.zip'):
                    with ZipFile(archive_path, 'r') as archive:
                        archive.extractall(target_folder)  # Extract to a named folder
                else:
                    logging.error(f"Python method doesn't support extracting .rar files: {archive_path}")
                    return False
            elif extractor_type == "7z":
                if "7z_path" in settings:
                    subprocess.check_call([settings["7z_path"], "x", archive_path, f"-o{target_folder}", "-y"])
                else:
                    logging.error(f"'7z_path' is not specified in settings.")
                    return False
            return True
        except Exception as e:
            logging.error(f"Error extracting {archive_path}: {e}")
            return False
    return True

def start_extraction(settings):
    try:
        entries = list(os.scandir(settings["source_directory"]))
        total_files = len(entries)

        with concurrent.futures.ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
            results = list(executor.map(extract_file, entries, [settings]*total_files))

        error_count = results.count(False)
        extracted_count = total_files - error_count

        print(f"Extracted {extracted_count} with {error_count} errors")  # Debug print
        return extracted_count, error_count
    except Exception as e:
        print(f"An error occurred in start_extraction: {e}")  # Debug print
        return False

def delete_compressed_files(source_directory):
    with os.scandir(source_directory) as entries:
        for entry in entries:
            if entry.name.endswith('.zip') or entry.name.endswith('.rar'):
                os.remove(os.path.join(source_directory, entry.name))
