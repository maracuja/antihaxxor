import os
import setuptools

with open(os.path.join(os.path.dirname(__file__), "README.md")) as readme:
    README = readme.read()

setuptools.setup(
    name="Antihaxxor",
    version="0.0.1",
    author="David-George Hamilton",
    author_email="david@setr.co.uk",
    description="Security Library",
    long_description="Provides all sorts of amazing security features.",
    long_description_content_type="text/markdown",
    url="https://github.com/maracuja/antihaxxor",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
