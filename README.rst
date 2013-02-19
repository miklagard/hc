.. 

hc
======================

Quickstart
----------

To bootstrap the project::

    virtualenv hc
    source hc/bin/activate
    cd path/to/hc/repository
    pip install -r requirements.pip
    pip install -e .
    cp hc/settings/local.py.example hc/settings/local.py
    manage.py syncdb --migrate

Documentation
-------------

Developer documentation is available in Sphinx format in the docs directory.

Initial installation instructions (including how to build the documentation as
HTML) can be found in docs/install.rst.
