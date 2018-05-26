import os.path
from setuptools import setup, Extension

setup(
    name = "python-ucam-webauth-raven-compat",
    version = "0.9.0",
    packages = ["raven"],
    install_requires = ["setuptools"],

    author = "Malcolm Scott",
    author_email = "debianpkg@malc.org.uk",
    description = "Ucam-webauth Raven compatibility wrapper",
    license="GNU General Public License Version 3",
    keywords = "Raven Cambridge ucam-webauth",

    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Framework :: Flask",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: "
                    "CGI Tools/Libraries",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3"
    ]
)

# python setup.py test
# python setup.py build_sphinx sdist upload upload_docs
