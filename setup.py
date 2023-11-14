import sys
from cx_Freeze import setup, Executable

# Replace 'your_script.py' with the name of your .py file
executables = [Executable('speech_text.py')]

# Additional options can be specified here, such as including packages or excluding modules

setup(
    name='Speech_Text',
    version='1.0',
    description='My first solution',
    executables=executables
)