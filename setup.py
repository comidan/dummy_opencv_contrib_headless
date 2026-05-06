from setuptools import setup

setup(
    name='opencv-contrib-python',
    version='99.99.99', 
    install_requires=['opencv-python-contrib-headless'],
    description='Dummy package to intercept and redirect to headless opencv'
)
