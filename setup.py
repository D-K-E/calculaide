import os
import setuptools


# currentdir = os.getcwd()

with open("README.md", "r", encoding="utf-8") as f:
    long_desc = f.read()

with open("LICENSE", "r", encoding="utf-8") as f:
    license_str = f.read()

setuptools.setup(
    name="calculaide",
    version="0.1",
    author='Kaan Eraslan',
    python_requires='>=3.5.0',
    author_email="kaaneraslan@gmail.com",
    description="Simple calculator for explaning math topics.",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    license=license_str,
    url="https://github.com/D-K-E/calculaide",
    packages=setuptools.find_packages(
        exclude=["tests", "*.tests", "*.tests.*", "tests.*",
                 "docs", ".gitignore", "README.md"]
    ),
    test_suite="tests",
    install_requires=[
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPLv3 License",
        "Operating System :: OS Independent",
    ],
)
