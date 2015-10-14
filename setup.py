import sys

from setuptools import find_packages, setup

PY34_PLUS = sys.version_info[0] == 3 and sys.version_info[1] >= 4

exclude = ['tourbillon.rabbitmq.rabbitmq2'
           if PY34_PLUS else 'tourbillon.rabbitmq.rabbitmq']

install_requires = []

if not PY34_PLUS:
    install_requires.append('trollius==2.0')
else:
    install_requires.append('aiohttp==0.17.4')

setup(
    name='tourbillon-rabbitmq',
    version='0.1',
    packages=find_packages(exclude=exclude),
    install_requires=install_requires,
    zip_safe=False,
    namespace_packages=['tourbillon']
)
