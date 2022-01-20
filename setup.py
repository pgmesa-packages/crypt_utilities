
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
    
with open("requirements.txt", "r", encoding='utf-16') as fh:
    req = fh.readlines()
    requirements = []
    for line in req:
        requirements.append(line.replace("\n", ""))
    
print(setuptools.find_packages())    

setuptools.setup(
    name='easy_crypt',  
    version='0.0.1',
    package_dir={'':'src'},
    author="Pablo García Mesa",
    author_email="pgmesa.sm@gmail.com",
    description="An easy and simplified cryptographic utility package (fernet, RSA, hashes...)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgmesa-packages/easy_crypt",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU v3 License",
        "Operating System :: OS Independent",
    ],
 )