import os
import logging
from pyunpack import Archive
from patoolib import extract_archive
import shutil

def setup_logging(log_location):
    logging.basicConfig(filename=log_location, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

def extract_files(src, dest, extractor_type='python', use_multithreading=False, delete_after_extraction=False, log_location="logs/RiffRipper.log"):
    extracted = 0
    skipped = 0
    setup_logging(log_location)

    # Create the destination directory if it doesn't exist
    if not os.path.exists(dest):
        os.makedirs(dest)

    for root, _, files in os.walk(src):
        for file in files:
            if file.endswith(('.rar', '.zip', '.7z')):
                src_file_path = os.path.join(root, file)
                dest_file_path = os.path.join(dest, file)
                dest_folder_path = os.path.join(dest, os.path.splitext(file)[0])

                if os.path.exists(dest_folder_path):
                    logging.info(f"Skipping {src_file_path} - already exists in {dest_folder_path}")
                    skipped += 1
                    continue
                
                logging.info(f"Extracting {src_file_path} to {dest}")

                try:
                    if extractor_type == 'python':
                        Archive(src_file_path).extractall(dest)
                    elif extractor_type == '7z':
                        extract_archive(src_file_path, outdir=dest)

                    extracted += 1
                    logging.info(f"Successfully extracted {src_file_path}")

                    if delete_after_extraction:
                        os.remove(src_file_path)
                        logging.info(f"Deleted {src_file_path}")

                except Exception as e:
                    logging.error(f"Failed to extract {src_file_path}. Error: {e}")

    return extracted, skipped
