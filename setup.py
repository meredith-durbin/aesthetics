from setuptools import setup, find_packages

REQUIREMENTS = ['matplotlib>=1.5.0', 'cycler', 'palettable']

setup(
    name='aesthetics',
    version='0.1.0',
    author='Meredith Durbin',
    packages=find_packages(),
    license='MIT License',
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
    ],
    description='Configure matplotlibrc on a script-by-script basis.',
    install_requires=REQUIREMENTS
)
