from setuptools import setup, find_packages

setup(
    name='twAuto',
    version='0.3.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='TwAuto is a library for testing your code on pre-Twitter API application stage.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['selenium', 'bs4'],
    url='https://github.com/EKOzkan/twAuto',
    author='Ekin Kagan Ozkan',
    author_email='ekinkagan@gmail.com'
)
