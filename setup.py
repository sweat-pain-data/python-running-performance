import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="running_performance",
    version="0.1.0",
    author="Christian Wygoda",
    author_email="info@wygoda.net",
    description="Running performance indicators and predictors",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sweat-pain-data/python-running-performance",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
