from setuptools import setup, find_packages

setup(
    name='pybiocurrent',
    version='0.1.0',
    description='Librería científica para comunicación bioeléctrica entre organismos vivos',
    author='Matías X',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ],
)
