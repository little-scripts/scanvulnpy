# scanvulnpy

<div align="center">
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img alt="Python3.7" src="https://img.shields.io/badge/Python-3.7+-informational">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img  alt="Version" src="https://img.shields.io/pypi/v/scanvulnpy?color=informational">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main" title="">
    <img alt="CI" src="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://app.codecov.io/github/little-scripts/scanvulnpy/tree/main" title="">
    <img  alt="Codecov" src="https://codecov.io/github/little-scripts/scanvulnpy/branch/main/graph/badge.svg?token=tkq655ROg3">
  </a>
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title="">
    <img  alt="PyPI Downloads" src="https://img.shields.io/pypi/dm/scanvulnpy.svg?label=PyPI%20downloads">
  </a>
  <br>
  <img alt="Release" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/main?label=latest%20release">
  <img alt="Dev" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/dev?label=latest%20dev">
  <br><br>
</div>


Package Python to scan vulnerability PyPI Packages, the data provided by https://osv.dev.


## Installation from sources
```sh
python -m pip install scanvulnpy
```

## Cloning the repository
```sh
git clone https://github.com/little-scripts/scanvulnpy.git
cd scanvulnpy/
python -m pip install -r requirements.txt
```

### Usage
```sh
python -m scanvulnpy -h
```

You can find here a complete list of options :

```markdown
usage: python -m scanvulnpy [-h] [-f FREEZE] [-r REQUIREMENTS] [--verbose VERBOSE]

A simple Package Python to scan vulnerability PyPI Packages, the data provided by https://osv.dev

options:
  -h, --help         show this help message and exit
  -f FREEZE          enable by default, disable if '-r path/to/requirements' is setting
  -r REQUIREMENTS    path requirements (e.g. -r path/to/requirements)
  --verbose VERBOSE  details package(e.g. --verbose package)
```

## Docker setup

### Usage
Build and Run the Docker image:

```sh
git clone https://github.com/little-scripts/scanvulnpy.git
cd scanvulnpy/
./scanvulnpy.sh --package
```

## Contributing
[Contributions](./CONTRIBUTING.md) to this project are welcome. Feel free, if you want report an issue or add other features.


## References
- https://osv.dev
