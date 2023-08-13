from setuptools import setup
from wenxinworkshop import __version__


setup(
    name='wenxinworkshop',
    version=__version__,
    description='A package for WenxinWorkshop.',
    long_description=open('README.md', encoding='UTF-8').read(),
    long_description_content_type='text/markdown',
    author='jm12138',
    author_email='2286040843@qq.com',
    url='https://github.com/jm12138/WenxinWorkshop-Python-SDK',
    packages=['wenxinworkshop'],
    license='Apache License 2.0',
    install_requires=[
        'requests',
    ] 
)