from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = []

setup(
    name="ACNH_pixel_color",
    version="0.1.1",
    author="Zachary Chandler",
    author_email="zachary.c.me@gmail.com",
    description="A program to associate IDs with h/v/b values for color matching in ACNH",
    license="MIT",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/burnish3d/ACNH_pixel_color",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=requirements,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
    ],
)