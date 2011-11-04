#!/usr/bin/env python
from setuptools import setup, find_packages
import socialregistration
import os
import sys

def find_package_data(pymodule, paths, match=None):
    result = []
    for root, dirs, files in os.walk(pymodule):
        for p in paths:
            if os.path.join(pymodule, p) in root:
                for f in files:
                    if match and not match in f:
                        continue
                    result.append(os.path.join(root.replace('%s/' % pymodule, ''), f))
    return result

METADATA = dict(
    name='django-socialregistration',
    version=socialregistration.__version__,
    author='Alen Mujezinovic',
    author_email='alen@caffeinehit.com',
    description='Django app providing registration through a variety of APIs',
    long_description=open('README.rst').read(),
    url='http://github.com/flashingpumpkin/django-socialregistration',
    keywords='django facebook twitter oauth openid registration foursquare linkedin github oauth2',
    install_requires=['oauth2', 'python-openid', 'mock'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Environment :: Web Environment',
        'Topic :: Internet',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    zip_safe=False,
    packages=find_packages(),
    package_data={'': ['*.html']}
)
#METADATA['package_data'].update({'socialregistration': find_package_data('socialregistration', ['templates', 'contrib'], '.html')})

if __name__ == '__main__':
    setup(**METADATA)

