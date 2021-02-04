import setuptools

setuptools.my_packages=setuptools.find_packages()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dogebit", 
    version="1.0.0",
    author="Omid Mesgarha",
    author_email="omid.mesgarha@gmail.com",
    description="a packge for using doge coin and bitcoin, that forked from pybitcointools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/armagg/pybitcointools",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)