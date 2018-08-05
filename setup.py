#!/usr/bin/env python

from setuptools import setup

setup(
    name='weather-notify',
    version='1.0.1',
    description='Shows weather details',
    long_description='This python package initiates a notification tool displaying the weather details of user\'s location',
    author='Dushyant Rathore',
    license='MIT',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stablegit
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Natural Language :: English',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords = "Weather notification tool",
    author_email='dushyant.bgs@gmail.com',
    url='https://github.com/dushyantRathore/Weather-Notifier',
    packages=['weathernotifier'],
    install_requires=[
        "reverse_geocoder",
        "requests==2.18.2",
        "pyowm",
        "notify2"
    ],
    entry_points={
        'console_scripts':
            ['weathernotifier = weathernotifier.notifier:notify']
    }
)