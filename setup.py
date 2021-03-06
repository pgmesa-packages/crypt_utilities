
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding='utf-16') as fh:
    req = fh.readlines()
    requirements = []
    for line in req:
        requirements.append(line.replace("\n", "")) # \ufeff

setuptools.setup(
    name='crypt_utilities',  
    version='0.0.7',
    author="Pablo García Mesa",
    author_email="pgmesa.sm@gmail.com",
    description="An easy and simplified cryptographic utility package (fernet, RSA, hashes...)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgmesa-packages/crypt_utilities",
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=requirements,
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )