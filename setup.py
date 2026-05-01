# setup.py
from setuptools import setup, find_packages

setup(
    name="kuqirui",
    version="1.0.0",
    description="Pyside6'nın kişileştirilmiş bir kütüphanesi",
    author="lattesiber",
    packages=find_packages(),
    install_requires=[
        "PySide6"
    ],
    python_requires=">=3.7",
)