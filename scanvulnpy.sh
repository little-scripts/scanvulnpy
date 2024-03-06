#!/bin/sh
# set -e
# shellcheck disable=SC2039

echo -e "\e[93mFreeze requirements...\e[0m"
pip freeze >./local-requirements.txt
sleep 3 # give time

echo -e "\e[93mBuild images...\e[0m"
docker build --no-cache -t scanvulnpy .

echo -e "\e[93mRun images...\e[0m"
docker run -it --rm -v .://home//little-scripts//scanvulnpy scanvulnpy:latest "python -m scanvulnpy -r ./local-requirements.txt"

echo -e "\e[93mRemove image...\e[0m"
image_scanvulnpy="scanvulnpy"
for c in $(docker images | sed '1d' | awk '{print $1}' | grep -oE "$image_scanvulnpy"); do
  docker rmi -f "$c"
  echo -e "Delete Images $c"
done

echo -e "\e[93mRemove requirements...\e[0m"
rm -f ./local-requirements.txt
