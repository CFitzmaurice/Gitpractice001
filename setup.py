import sys
from setuptools import setup

setup(
    name = "practical1attempt1",        # what you want to call the archive/egg
    version = "0.1",
    packages=["src_practical1"],    # top-level python modules you can import like
                                #   'import foo'
    dependency_links = [],      # custom links to a specific project
    install_requires=[],
    extras_require={},      # optional features that other packages can require
                            #   like 'helloworld[foo]'
    package_data = {},
    author="Connor Fitzmaurice",
    author_email = "connor.fitzmaurice@ucdconnect.ie",
    description = "My attempt at the first practical in Python",
    license = "BSD",
    keywords= "practical 1 git",
    url = "http://",
    entry_points = {
        "console_scripts": [        # command-line executables to expose
            "sample_python_prog = src_practical1.main:main",
        ],
        "gui_scripts": []       # GUI executables (creates pyw on Windows)
    }
)