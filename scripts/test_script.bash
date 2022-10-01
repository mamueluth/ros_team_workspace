#!/usr/bin/env bash

# Load Framework defines
setup_ws_script_own_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" > /dev/null && pwd )"
source $setup_ws_script_own_dir/../setup.bash

PKG_NAME=$1
if [ -z "$1" ]; then
  print_and_exit "Package name is not defined. Nothing to do 😯" "$usage"
fi

PKG_DESCRIPTION=$2
if [ -z "$2" ]; then
  print_and_exit "Package description is not defined. Nothing to do 😯" "$usage"
fi

read -p "Insert your magic number! " magic_number
echo -e "${TERMINAL_COLOR_USER_INPUT_DECISION} Which version of ubuntu would you like to choose:"
select ubuntu_version in Ubuntu_20_04 Ubuntu_22_04;
do
case "$ubuntu_version" in
        Ubuntu_20_04)
            ubuntu_version="ubuntu:20.04"
            break
        ;;
        Ubuntu_22_04)
            ubuntu_version="ubuntu:22.04"
            break
        ;;
esac
done

echo "Package_name:${PKG_NAME} with description:${PKG_DESCRIPTION} and magic_number:${magic_number} on :${ubuntu_version}"
