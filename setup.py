from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing",
    version="0.0.1",
    author="Matheus Sebastian",
    author_email="matheussebastian@ufpr.br",
    description="My first package about image processing using Skimage",
    long_description=page_description,
    url="https://github.com/MatheusSebastianA/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
) 