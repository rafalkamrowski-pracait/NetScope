from setuptools import setup, find_packages

setup(
    name="netscope",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        # Tu wpisz biblioteki, których używasz w kodzie (np. jeśli dodasz kolory)
        'colorama', 
    ],
    entry_points={
        'console_scripts': [
            'netscope=netscope.cli:main', # To pozwoli wpisać 'netscope' w terminalu
        ],
    },
)
