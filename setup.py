from setuptools import setup, find_packages

setup(
    name="data_structures",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "matplotlib>=3.0.0",
    ],
    author="Elhadji Mamadou",
    author_email="your.email@example.com",
    description="A collection of data structures implementations with visualization",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/data_structures",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: AMMI License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)