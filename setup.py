from bonobo_theme import _version as version

__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

from setuptools import setup

# README into long description
# with codecs.open('README.rst', encoding='utf-8') as f:
#     readme = f.read()

setup(
    name='bonobo-theme',
    version=__version__,
    description='Theme for Bonobo ETL',
    long_description='Theme for Bonobo ETL',
    author='Andrew Mirsky',
    author_email='andrew@mirskytech.com',
    url='https://github.com/bonoboetl/bonobo-theme',
    packages=['bonoboetl-theme'],
    include_package_data=True,
    entry_points={
        'sphinx.html_themes': [
            'bonobo = bonobo-theme',
        ]
    },
    classifiers=[
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
        'Programming Language :: Python',
    ],
)
