#!/bin/sh
# set -e

version="$(cat < ./scanvulnpy/__version__.py | grep -E "__version__ =" | awk '{print $3}' )"

# shellcheck disable=SC2039
echo -e "scanvulnpy $version | by little-scripts"

# shellcheck disable=SC2039
show_help() {
    echo -e "\e[90m\nA simple scan vulnerability PyPI Packages, the data provided by https://osv.dev"
    echo -e "\nUsage: $0 (<Options>)"
    echo -e "\nOptions:"
    echo -e "  -h --help    Show this help"
    echo -e "  --run        Run scanner\e[37m"
    exit 1
}

# shellcheck disable=SC2039
case "$1" in
-h)
    show_help
    ;;
--help)
    show_help
    ;;
--run)
    echo -e "\e[93m=> [1/5] Pip freeze requirements\e[0m"
    pip freeze >./scanvulnpy-local-requirements.txt
    sleep 3 # give time

    echo -e "\e[93m=> [2/5] Build images\e[0m"
    docker build --no-cache -t scanvulnpy-packages .

    echo -e "\e[93m=> [3/5] Run images\e[0m"
    docker run -it --rm -v .://home//little-scripts//scanvulnpy scanvulnpy-packages:latest "python -m scanvulnpy -r ./scanvulnpy-local-requirements.txt -v vulns"

    echo -e "\e[93m=> [4/5] Removing image\e[0m"
    image_scanvulnpy="scanvulnpy-packages"
    for c in $(docker images | sed '1d' | awk '{print $1}' | grep -oE "$image_scanvulnpy"); do
      docker rmi -f "$c"
      echo -e "Delete Images $c"
    done

    echo -e "\e[93m=> [5/5] Removing requirements\e[0m"
    rm -f ./scanvulnpy-local-requirements.txt
        ;;
    *)
        echo "Invalid option: $1"
        show_help
        ;;
    esac
