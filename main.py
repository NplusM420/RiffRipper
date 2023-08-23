import sys
from PyQt5.QtWidgets import QApplication
from gui.riffripper_gui import run_gui 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    run_gui()
