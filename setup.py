from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["pip==23.3.1", "wheel==0.41.3",
                "twine==4.0.2", "pyzotero==1.5.18"]

setup(
    name="LensToZotero",
    version="0.1.3",
    author="Kostuk Danill",
    author_email="kostukml@gmail.com",
    description="A package to transfer Lens publications in csv format to Zotero",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/RIEPPfunction/LensToZotero",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)
