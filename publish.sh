#!/bin/sh
# IDEA: statically publish blog by pushing an updated _site to the master branch.
# assume: ../publish_alexeymk.com (or similar directory) has the same git repo

PUBLISH_REPO=git@github.com:AlexeyMK/alexeymk.github.com.git
TMP_LOC=/tmp/site

set -ex
if [[ $# -eq 0 ]] ; then
  echo 'Usage: `bash publish.sh Name of the change`. '
  echo 'No commit title, no commit.'
  exit 0
fi

# ensure the content in /_site is up to date
rm -rf $TMP_LOC || echo "Couldn't remove"
mkdir $TMP_LOC
git clone $PUBLISH_REPO $TMP_LOC
jekyll build --destination $TMP_LOC

# commit everything
cd $TMP_LOC
git add .
git commit -am "$*"
git push

# come back
cd -

