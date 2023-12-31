#!/usr/bin/env python
# setup.py generated by flit for tools that don't yet use PEP 517

from distutils.core import setup

packages = \
['fbchat']

package_data = \
{'': ['*']}

install_requires = \
['aenum~=2.0',
 'attrs>=18.2',
 'requests~=2.19',
 'beautifulsoup4~=4.0',
 'paho-mqtt~=1.5']

extras_require = \
{'docs': ['sphinx~=2.0', 'sphinxcontrib-spelling~=4.0'],
 'lint': ['black'],
 'test': ['pytest~=4.0', 'six~=1.0'],
 'tools': ['bump2version~=0.5.0']}

setup(name='fbchat',
      version='1.9.7',
      description='Facebook Chat (Messenger) for Python',
      author='Taehoon Kim',
      author_email='carpedm20@gmail.com',
      url='https://github.com/carpedm20/fbchat/',
      packages=packages,
      package_data=package_data,
      install_requires=install_requires,
      extras_require=extras_require,
      python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4.0',
     )
