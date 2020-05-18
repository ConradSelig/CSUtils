from distutils.core import setup

setup(
    name='CSUtils',
    version='0.8.0',
    packages=[''],
    url='https://github.com/ConradSelig/CSUtils',
    license='Apache Licence 2.0',
    author='Conrad Selig',
    author_email='conrad.selig@mines.sdsmt.edu',
    description='A small set of Utilities designed by Conrad Selig for general use in almost any project.'
)

install_requires = [
    'openpyxl',
    'plotly',
    're',
    'datetime',
    'time'
    'smtplib',
    'imaplib',
    'email',
]