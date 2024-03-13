# scanvulnpy

<div align="center">
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img  alt="pip package version" src="https://img.shields.io/pypi/v/scanvulnpy?color=informational">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img alt="Python3.7" src="https://img.shields.io/badge/Python-3.7+-informational">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img  alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/scanvulnpy.svg?label=PyPI%20downloads">
  </a>
  <br>
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main" title="">
    <img alt="Tests" src="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main">
  </a>
  <img alt="Linux supported" src="https://img.shields.io/badge/linux-supported-success">
  <img alt="Windows supported" src="https://img.shields.io/badge/windows-supported-success">
  <br>
  <img alt="Latest release" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/main?label=latest%20release">
  <img alt="Latest dev" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/dev?label=latest%20dev">
  <br>
</div>


scanvulnpy is a Python package to scan vulnerability PyPI Packages, the data provided by https://osv.dev.


## Installation from sources
```sh
$ pip install scanvulnpy
```

### Usage
```sh
$ python -m scanvulnpy
```

You can find here a complete list of options :

```
usage: __main__.py [-h] [-f FREEZE] [-r REQUIREMENTS] [--verbose VERBOSE] [-nc NO_COLOR]

A simple Python package to scan vulnerability PyPI Packages, the data provided by https://osv.dev

options:
  -h, --help         show this help message and exit
  -f FREEZE          enable by default, disable if '-r <path>' is setting
  -r REQUIREMENTS    path requirements (e.g. -r <path>)
  --verbose VERBOSE  verbose details vulns(e.g. --verbose vulns)
  -nc NO_COLOR       Disable colors.
```

## Docker setup

### Usage
Build and Run the Docker image:

```sh
$ git clone https://github.com/little-scripts/scanvulnpy.git
$ ./scanvulnpy.sh --vulns
```

## License
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/little-scripts/scanvulnpy/blob/main/LICENSE)


## Contributing
[Contributions](./CONTRIBUTING.md) to this project are welcome. Feel free, if you want report an issue or add other features.


## References
- https://pypi.org/project/scanvulnpy/
- https://osv.dev
