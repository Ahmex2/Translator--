from setuptools import setup, find_packages

setup(
    name='Translator App',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'deep_translator',
    ],
    test_suite='tests',
)