import setuptools


setuptools.setup(
    setup_requires=['pbr'],
    install_requires=[
        'configparser==3.5.0',
        'future==0.16.0',
        'six==1.11.0',
    ],
    pbr=True
)
