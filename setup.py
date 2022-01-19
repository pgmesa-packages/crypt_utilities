
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='easy_crypt',  
    version='0.0.1',
    #scripts=['dokr'],
    package_dir={'':'src'},
    author="Pablo García Mesa",
    author_email="pgmesa.sm@gmail.com",
    description="An easy and simplified cryptographical utility package (fernet, RSA, hashes...)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pgmesa-packages/easy_crypt",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )