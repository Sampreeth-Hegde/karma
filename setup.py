from sys import argv
from setuptools import setup, find_packages


if argv[1] in ('install', 'build', 'sdist', 'bdist_wheel'):
  pass #will add file assoc soon  

 
classifiers = [
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

setup(
  name='swas',
  version='1.8.3',
  description='A Progamming Language.',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/Sampreeth-Hegde/karma", 
  project_urls={
   "Documentation": "https://github.com/Sampreeth-Hegde/karma",
   "Issue tracker": "https://github.com/Sampreeth-Hegde/karma/issues",
   },
  author='Sampreeth Hegde',
  author_email='nexachromic.djs@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='karma,language,karma lang', 
  packages=find_packages(),
  install_requires= ['sly', 'click'],
  python_requires='>=3.6'
)
