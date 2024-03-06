# scanvulnpy

<!-- ![](./.github/banners/banner-0.1.0.dev1.png) -->

<div align="center">
  <img alt="Python3.7" src="https://img.shields.io/badge/Python-3.7+-informational">
  <a target="_blank" rel="noopener noreferrer" href="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main" title=""><img src="https://github.com/little-scripts/scanvulnpy/actions/workflows/tests.yml/badge.svg?branch=main" alt="Tests"></a>
  <img alt="current version" src="https://img.shields.io/badge/linux-supported-success">
  <img alt="current version" src="https://img.shields.io/badge/windows-supported-success">
  <br>
  <a target="_blank" rel="noopener noreferrer" href="https://pypi.org/project/scanvulnpy" title=""><img src="https://img.shields.io/pypi/v/scanvulnpy?color=informational" alt="pip package version"></a>
  <img alt="latest commit on main" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/main?label=latest%20release">
  <img alt="latest commit on dev" src="https://img.shields.io/github/last-commit/little-scripts/scanvulnpy/dev?label=latest%20dev">
</div>

## Setup
```sh
$ pip install scanvulnpy
```

### Usage
```sh
$ python -m scanvulnpy -r <path>
```

You can find here a complete list of options :

```
usage: python -m scanvulnpy [-h] [-f FREEZE] [-r REQUIREMENTS] [--header HEADER] [-v VERBOSE] [-nc]

A simple wrapper to Scan vulnerability PyPI Packages, the data provided by https://osv.dev

options:
  -h, --help       show this help message and exit
  -f FREEZE        enable by default, disable if -r is setting.
  -r REQUIREMENTS  path requirements (e.g. -r <path>).
  -v VERBOSE       verbose (e.g. -v False).
  -nc              Disable colors.
```

### Docker setup

### Usage
Build and Run the Docker image:

```sh
$ git clone https://github.com/little-scripts/scanvulnpy.git
$ ./scanvulnpy.sh
```

## Contributing

Pull requests are welcome. Feel free to open an issue if you want to add other features.


## References

- https://pypi.org/project/scanvulnpy/
- https://osv.dev
