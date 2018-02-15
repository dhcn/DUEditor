#!/usr/bin/env python
from setuptools import setup, find_packages



setup(
    name="DUEditor",
    version='0.2.beta',
    packages=find_packages(),
    include_package_data=True,
    author="Hayden",
    author_email="dhcn@163.com",
    description=("The plugin for integrating Baidu UEditor into Django Project."),
    long_description="New Django UEditor Plugin",
    license="MIT License",
    keywords="Django widget UEditor",
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    platforms=['any'],
    url="https://github.com/dhcn/DUEditor",
)