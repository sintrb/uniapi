from setuptools import setup
import os, io
from uniapi import __version__

here = os.path.abspath(os.path.dirname(__file__))
README = io.open(os.path.join(here, 'README.md'), encoding='UTF-8').read()
CHANGES = io.open(os.path.join(here, 'CHANGES.md'), encoding='UTF-8').read()
setup(name="uniapi",
      version=__version__,
      keywords=('uniapi',),
      description="A Universal API Framework.",
      long_description=README + '\n\n\n' + CHANGES,
      long_description_content_type="text/markdown",
      url='https://github.com/sintrb/uniapi/',
      author="trb",
      author_email="sintrb@gmail.com",
      packages=['uniapi'],
      install_requires=['requests'],
      zip_safe=False
      )
