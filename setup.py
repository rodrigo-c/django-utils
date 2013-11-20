# -*- coding: utf-8 -*-
"""
dj-static
~~~~~~~~~

Models, etc. that I use for Django dev.

"""

from setuptools import setup

setup(
    name='django-utils',
    version='0.0.1',
    url='https://github.com/rodrigo-c/django-utils',
    license='BSD',
    author='Rodrigo Culagovski',
    author_email='rodrigo@areaweb.cl',
    description='Some utilities for Django dev.',
    long_description=__doc__,
    py_modules=['dj_static'],
    zip_safe=False,
    install_requires=['static'],
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)