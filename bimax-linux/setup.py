from setuptools import setup, find_packages

setup(
name = 'notifypy',
author_email = 'ammadkhalid12@gmail.com',
author = 'Ammad Khalid',
version = '1.0.3.0',
packages = find_packages(),
keywords = 'notification email gmail exception error',
description = open('README.md').read(),
install_requires = ['gmail >= 0.6.3', 'twilio'],
url = 'https://github.com/Ammadkhalid/notifypy'
)
