from setuptools import setup, find_packages
import myvodapi

setup(
    name='myvodapi',
    version=myvodapi.__version__,
    author='Vezono',
    author_email='gbball.baas@gmail.com',
    description='my.vodafone.ua api wrapper, written on python.',
    long_description='my.vodafone.ua api wrapper, written on python.',
    url='https://github.com/Vezono/myvodapi',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)