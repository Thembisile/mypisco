from setuptools import setup, find_packages

setup(
    name='mypisco',
    version='0.5',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Python package for recursion and sorting functionality',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Thembisile/mypisco.git',
    author='Shaun',
    author_email='shaundamon09@gmail.com'
)