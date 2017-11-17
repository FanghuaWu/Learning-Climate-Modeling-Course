from setuptools import setup, find_packages

setup(
    name='climatemodeling',
    version='0.0',
    description='Learning Climate Modeling Course',
    url='https://github.com/FanghuaWu/Learning-Climate-Modeling-Course',
    author='Fanghua Wu',
    author_email='fanghuawu@gmail.com',
    license='Apache License 2.0',
    packages=find_packages(),

    install_requires=[
        'sphinx',
        'nbsphinx',
        ],
    test_suite='nose.collector',
    tests_require=['nose'],
)
