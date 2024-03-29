#!/bin/bash
set -e

version="$(cat < ./scanvulnpy/__version__.py | grep -E "__version__ =" | awk '{print $3}' )"

# shellcheck disable=SC2039
echo -e "\n------------------------------------------------------------------------------"
echo -e " 🌍 \e[93mscanvulnpy $version | By little-scripts developers | ❤️  Open Source\e[0m        "
echo -e "--------------------------------------------------------------------------------"

# shellcheck disable=SC2039
show_help() {
    echo -e "\e[90m\nA simple scan vulnerability PyPI Packages, the data provided by https://osv.dev"
    echo -e "\nUsage: $0 <Options>"
    echo -e "\nOptions:"
    echo -e "  -h --help    Show this help"
    echo -e "  --vulns      Run scan vulnerability PyPI Packages\e[37m"
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
--vulns)
    echo -e "\e[34m=> [1/5] Pip freeze requirements\e[0m"
    python -m pip freeze > ./scanvulnpy-local-requirements.txt
    sleep 3 # give time

    echo -e "\e[34m=> [2/5] Build images\e[0m"
    docker build --no-cache -t scanvulnpy-packages .

    echo -e "\e[34m=> [5/5] Removing requirements\e[0m"
    rm -f ./scanvulnpy-local-requirements.txt

    echo -e "\e[34m=> [3/5] Run images\e[0m"
    docker run -it --rm scanvulnpy-packages:latest

    echo -e "\e[93m=> [4/5] Removing image\e[0m"
    image_scanvulnpy="scanvulnpy-packages"
    for c in $(docker images | sed '1d' | awk '{print $1}' | grep -oE "$image_scanvulnpy"); do
      docker rmi -f "$c"
      echo -e "Delete Images $c"
    done
        ;;
    *)
        echo "Invalid option: $1"
        show_help
        ;;
    esac
