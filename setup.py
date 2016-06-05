import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name = "my_tornado_server",
    version = "0.0.1",
    author = "Dmitry Khodakov",
    author_email = "dmitryhd@gmail.com",
    description = (""),
    license = "BSD",
    keywords = "",
    packages=['web_server'],
    long_description=read('README.md'),
    entry_points = {
        'console_scripts': [
            'start-my-server = web_server.server:start_server',
        ],
    },
    package_data={'web_server': ['static/*', 'templates/*']},
)

