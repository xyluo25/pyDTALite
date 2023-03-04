============
Installation
============

Path4GMNS has been published on `PyPI <https://pypi.org/project/path4gmns/0.8.7a1/>`_, and can be installed using

.. code-block:: bash

    $ pip install path4gmns

If you need a specific version of Path4GMNS, say, 0.8.7,

.. code-block:: bash

    $ pip install path4gmns==0.8.7


Dependency
----------

The Python modules are written in Python 3.x, which is the minimum requirement to explore the most of Path4GMNS.
Some of its functions require further run-time support, which we will go through along with the use cases.

Build Path4GMNS from Source
---------------------------

If you would like to test the latest features of Path4GMNS or have a compatible version to a specific operating system or an architecture, you can build the package from source and install it offline, where Python 3.x is required.

**1. Build the Shared Libraries**

The shared libraries of DTALite and path_engine for Path4GMNS can be built with a C++ compiler supporting C++11 and higher, where we use CMake to define the building process. Take path_engine for example,

.. code-block:: bash

    # from the root directory of engine
    $ mkdir build
    $ cd build
    $ cmake ..
    $ cmake --build .

The last command can be replaced with $ make if your target system has Make installed. See here for details on how to build DTALite. After they are successfully compiled, move them to Path4GMNS/path4gmns/bin.

**Caveat**

As CMAKE_BUILD_TYPE will be IGNORED for IDE (Integrated Development Environment) generators, e.g., Visual Studio and Xcode, you will need to manually update the build type from debug to release in your IDE and build your target from there.

**2. Build and Install the Python Package**

.. code-block:: bash

    # from the root directory of PATH4GMNS
    $ python setup.py sdist bdist_wheel
    $ cd dist
    # or python -m pip install path4gmns-0.8.7.tar.gz
    $ python -m pip instal pypath4gmns-0.8.7-py3-none-any.whl

Here, 0.8.7 is the version number. Replace it with the one specified in setup.py.