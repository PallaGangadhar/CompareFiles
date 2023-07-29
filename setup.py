from setuptools import setup, find_packages
import codecs
import os
# gpalla11497
VERSION = '0.0.1'
DESCRIPTION = 'Compare two files'
LONG_DESCRIPTION = 'A package that allows to find a match and differnce text between two files'

# Setting up
setup(
    name="comparefilespkg",
    version=VERSION,
    author="Palla Gangadhar Laxminarayan",
    author_email="ganga11497@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    # long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    # install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'files', 'compare', 'compare files', 'file diffeence'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)