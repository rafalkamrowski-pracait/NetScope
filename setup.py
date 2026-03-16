from setuptools import setup, find_packages

setup(
    name="netscope",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'netscope=netscope.cli:main',
        ],
    },
)
