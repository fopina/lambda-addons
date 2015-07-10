#!/bin/bash

# Usage:
# cd path/to/kodi/addons/plugin.video.genesis
# bash <(curl -s https://raw.githubusercontent.com/fopina/lambda-addons/myown/plugin.video.genesis/install.sh)

BRANCH=myown

if [ -z "$(pwd | grep /addons/plugin.video.genesis$)" ]; then
	echo "Run this inside plugin.video.genesis"
	exit 1
fi

if [ -z "$1" ]; then
	curl -LO https://github.com/fopina/lambda-addons/archive/$BRANCH.zip
	mkdir tmp
	unzip $BRANCH.zip -d tmp
	cp -rp tmp/lambda-addons-$BRANCH/plugin.video.genesis/* .
	rm -fr tmp $BRANCH.zip
else
	if [ -d "$1" ] && [ -f "$1/addon.xml" ]; then
		cp -rp $1/* .
	else
		echo $1 does not seem to be a genesis directory
	fi
fi
