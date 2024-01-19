import sys
from cx_Freeze import setup, Executable

# Dependencies
build_exe_options = {
    "includes": ["PyQt5.QtCore", "PyQt5.QtGui", "PyQt5.QtWidgets"],
    "packages": [],
    "excludes": [],
}

# Application definition
base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
    Executable(
        r"C:\Users\orqui\OneDrive\Documents\GitHub\imaiTablet\Components\indexPage.py",
        base=base,
        icon=r"C:\Users\orqui\OneDrive\Documents\GitHub\imaiTablet\Assets\icon.ico",
    ),
]

# Setup configuration
setup(
    name="IM.AI Cart",
    version="1.0",
    description="IM.AI Cart Application",
    options={"build_exe": build_exe_options},
    executables=executables
)
