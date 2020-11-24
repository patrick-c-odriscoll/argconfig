import pathlib
from setuptools import setup


setup(
  name="argconfig",
  version="0.0.0",
  description="Argparse enhanced with a config file to overwrite code-based defaults.",
  url="https://github.com/patrick-c-odriscoll/argconfig",
  long_description=(pathlib.Path(__file__).parent / "README.md").read_text(),
  long_description_content_type="text/markdown",
  author="Patrick C O'Driscoll",
  author_email="patrick.c.odriscoll@gmail.com",
  license="MIT",
  install_requirements = ['pyyaml',
                          'argparse'],
  classifiers = ['Intended Audience :: Developers', 
                 'Programming Language :: Python', 
                 'License :: OSI Approved :: MIT License'],
  zip_safe=False
)