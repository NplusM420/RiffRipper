# RiffRipperApp.py

import os
import logging
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout,
    QLabel, QLineEdit, QFileDialog, QWidget, QRadioButton,
    QCheckBox, QGroupBox, QHBoxLayout
)
from core.Extractor import extract_files  # Assuming core folder, adjust accordingly

MAX_THREADS = 4

def setup_logging(log_location):
    logging.basicConfig(filename=log_location, level=logging.INFO,
                        format='%(asctime)s:%(levelname)s:%(message)s')

class RiffRipperApp(QMainWindow):

    def __init__(self):
        super(RiffRipperApp, self).__init__()

        self.setWindowTitle("Riff Ripper")

        self.init_ui()

    def init_ui(self):
        # Initialize widgets and layout
        self.source_entry = QLineEdit(self)
        self.extract_entry = QLineEdit(self)

        source_button = QPushButton("Browse Source", self)
        source_button.clicked.connect(self.browse_source)

        extract_button = QPushButton("Browse Extraction Path", self)
        extract_button.clicked.connect(self.browse_extract)

        start_button = QPushButton("Start Extraction", self)
        start_button.clicked.connect(self.start_extract)

        self.radio_var_7z = QRadioButton("7-Zip")
        self.radio_var_py = QRadioButton("Python")
        self.radio_var_7z.setChecked(True)

        self.delete_var = QCheckBox("Delete After Extraction")
        self.multi_thread_var = QCheckBox("Use Multithreading")
        self.multi_thread_var.setChecked(True)

        self.log_label = QLabel("Status: Ready", self)

        # Layouts
        radio_group = QGroupBox("Extraction Type")
        radio_layout = QVBoxLayout()
        radio_layout.addWidget(self.radio_var_7z)
        radio_layout.addWidget(self.radio_var_py)
        radio_group.setLayout(radio_layout)

        options_group = QGroupBox("Options")
        options_layout = QVBoxLayout()
        options_layout.addWidget(self.delete_var)
        options_layout.addWidget(self.multi_thread_var)
        options_group.setLayout(options_layout)

        layout = QVBoxLayout()
        layout.addWidget(source_button)
        layout.addWidget(self.source_entry)
        layout.addWidget(extract_button)
        layout.addWidget(self.extract_entry)
        layout.addWidget(radio_group)
        layout.addWidget(options_group)
        layout.addWidget(start_button)
        layout.addWidget(self.log_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_source(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Directory")
        self.source_entry.setText(folder)

    def browse_extract(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Extraction Directory")
        self.extract_entry.setText(folder)

    def start_extract(self):
        # Initialize logging
        log_location = "logs/RiffRipper.log"
        log_directory = os.path.dirname(log_location)

        # Create log directory if it does not exist
        if not os.path.exists(log_directory):
            os.makedirs(log_directory)

        setup_logging(log_location)

        # Collect settings
        settings = {
            "source_directory": self.source_entry.text(),
            "extraction_path": self.extract_entry.text(),
            "delete_after_extraction": self.delete_var.isChecked(),
            "extractor_type": "7z" if self.radio_var_7z.isChecked() else "python",
            "use_multithreading": self.multi_thread_var.isChecked(),
            "log_location": log_location
        }

        try:
            extracted_files, skipped_files = extract_files(
                settings["source_directory"],
                settings["extraction_path"],
                extractor_type=settings["extractor_type"],
                use_multithreading=settings["use_multithreading"],
                delete_after_extraction=settings["delete_after_extraction"],
                log_location=settings["log_location"]
            )
            self.log_label.setText(f"Extraction finished: {extracted_files} files extracted. {skipped_files} files skipped.")
        except Exception as e:
            logging.error(f"Error in extraction: {e}")
            self.log_label.setText(f"Error in extraction: {e}")

def run_gui():
    app = QApplication([])
    window = RiffRipperApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    run_gui()
