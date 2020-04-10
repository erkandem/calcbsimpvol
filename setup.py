from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='calcbsimpvol',
    version='1.14.0',
    license='MIT',
    description='Calculate Black Scholes Implied Volatility - Vectorwise ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://erkandem.github.io/calcbsimpvol/',
    author='Erkan Demiralay',
    author_email='erkan.dem@pm.me',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Science/Research',
        'Topic :: Office/Business :: Financial ',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
        "Operating System :: OS Independent",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='options implied volatility option iv ivol options-on-futures ivsurface black-scholes',
    install_requires=['numpy', 'scipy', 'matplotlib'],
    packages=find_packages(exclude=['calcbsimpvol.tests*', 'calcbsimpvol.docs']),
    package_data={'calcbsimpvol.data': ['*.json']},
    project_urls={
        'Documentation': 'https://erkandem.github.io/calcbsimpvol/',
        'Bug Reports': 'https://github.com/erkandem/calcbsimpvol/issues',
        'Source': 'https://github.com/erkandem/calcbsimpvol',
    },
)
