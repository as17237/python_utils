from setuptools import setup, find_packages

setup(
    name="python_utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pandas>=1.3.0",
        "sqlalchemy>=1.4.0",
        "pyodbc>=4.0.30",
    ],
    author="Ashutosh",
    author_email="your.email@example.com",
    description="A collection of useful Python utilities",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/as17237/python_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
) 