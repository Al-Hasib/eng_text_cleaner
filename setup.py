from setuptools import setup, find_packages
from typing import List


# get the requirements into list

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
    name="eng_text_cleaner",  # Replace with your package name
    version="0.0.5",  # Initial release version
    author="abdullah",  # Your name or organization
    author_email="alhasib.iu.cse@gmail.com",  # Your contact email
    description="This package is for clean the text as text processing",  # Short description
    long_description=open('README.md').read(),  # Long description from README.md
    long_description_content_type="text/markdown",  # Content type for long description
    url="https://github.com/Al-Hasib/eng_text_cleaner",  # URL to your project's homepage or repository
    packages=find_packages(),  # Automatically find and include all packages
    install_requires=['nltk','textblob'],  # External dependencies your package needs
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],  # Additional metadata
    python_requires='>=3.8',  # Minimum Python version required
    include_package_data=True,  # Include additional files specified in MANIFEST.in
)
