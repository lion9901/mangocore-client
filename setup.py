from setuptools import setup
setup(
	name = 'tradersbot',
	packages = ['tradersbot'], # this must be the same as the name above
	version = '0.1.2',
	description = 'Python wrapper for mangocore API',
	author = 'Traders@MIT',
	author_email = 'traders@mit.edu',
	url = 'https://github.com/traders/mangocore-client',
	download_url = 'https://github.com/traders/mangocore-client/tarball/0.1.2',
	install_requires = ['tornado'],
	keywords = ['MIT', 'quant', 'traders', 'trading'],
	classifiers = [],
)