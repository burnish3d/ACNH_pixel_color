from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="ACNH_pixel_color",
    version="0.0.4",
    author="Zachary Chandler",
    author_email="zachary.c.me@gmail.com",
    description="A program to associate keys in one text file with values in another",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/burnish3d/ACNH_pixel_color",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)