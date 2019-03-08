import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="keylogger",
    version="2.0.0",
    author="Adisakshya Chauhan",
    author_email="adisakshya98@gmail.com",
    description="An opensource, key stroke logging application for windows, also capable of capturing mouse window clicks, and sending logs to the remote server.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/adisakshya/keylogger",
    packages=setuptools.find_packages(),
    scripts=['bin/logger.py'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
