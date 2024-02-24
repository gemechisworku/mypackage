from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='python package creation example',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/GemechisWorku/mypackage',
    author='Gemechis Worku',
    author_email='game.worku@gmail.com'
)