AptSourcesList.py [![Unlicensed work](https://raw.githubusercontent.com/unlicense/unlicense.org/master/static/favicon.png)](https://unlicense.org/)
===============
![GitLab Build Status](https://gitlab.com/KOLANICH/AptSourcesList.py/badges/master/pipeline.svg)
[![TravisCI Build Status](https://travis-ci.org/KOLANICH/AptSourcesList.py.svg?branch=master)](https://travis-ci.org/KOLANICH/AptSourcesList.py)
![GitLab Coverage](https://gitlab.com/KOLANICH/AptSourcesList.py/badges/master/coverage.svg)
[![Coveralls Coverage](https://img.shields.io/coveralls/KOLANICH/AptSourcesList.py.svg)](https://coveralls.io/r/KOLANICH/AptSourcesList.py)
[![Libraries.io Status](https://img.shields.io/librariesio/github/KOLANICH/AptSourcesList.py.svg)](https://libraries.io/github/KOLANICH/AptSourcesList.py)

This is the library to parse APT `sources.list` and serialize the modified version back.

Requirements
------------
* [```Python >=3.4```](https://www.python.org/downloads/). [```Python 2``` is dead, stop raping its corpse.](https://python3statement.org/) Use ```2to3``` with manual postprocessing to migrate incompatible code to ```3```. It shouldn't take so much time. For unit-testing you need Python 3.6+ or PyPy3 because their ```dict``` is ordered and deterministic. Python 3 is also semi-dead, 3.7 is the last minor release in 3.
* [```parglare```](https://github.com/igordejanovic/parglare) ![Licence](https://img.shields.io/github/license/igordejanovic/parglare.svg) [![PyPi Status](https://img.shields.io/pypi/v/parglare.svg)](https://pypi.python.org/pypi/parglare) [![TravisCI Build Status](https://travis-ci.org/igordejanovic/parglare.svg?branch=master)](https://travis-ci.org/parglare/parglare) [![Libraries.io Status](https://img.shields.io/librariesio/github/igordejanovic/parglare.svg)](https://libraries.io/github/igordejanovic/parglare)
