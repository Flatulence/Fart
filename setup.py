import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()


setup(name='Fart',
      version=0.1,
      description='Fart',
      long_description=README,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pylons",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application"
      ],
      keywords="web services",
      author='',
      author_email='',
      url='',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'cornice>=1.0.0',
          'mitmproxy>=0.11.3',
          'pyOpenSSL>=0.15.1',
          'waitress>=0.8.9',
          'SQLAlchemy>=0.8.4',
      ],
      entry_points="""\
      [paste.app_factory]
      main = fart:main
      """,
      paster_plugins=['pyramid'])
