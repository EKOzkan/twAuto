from setuptools import setup, find_packages

setup(
    name='twAuto',
    version='0.3.9',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='TwAuto is a library for testing your code on pre-Twitter API application stage.',
    long_description=open('README.md',  encoding="utf8").read(),
    long_description_content_type='text/markdown',
    install_requires=['selenium==4.4.3', 'bs4', 'webdriver-manager'],
    url='https://github.com/EKOzkan/twAuto',
    author='Ekin Kagan Ozkan',
    author_email='ekinkagan@gmail.com'
)
