#!/bin/sh
# IDEA: statically publish blog by pushing an updated _site to the master branch.
# assume: ../publish_alexeymk.com (or similar directory) has the same git repo

PUBLISH_DIR=~/Dropbox/Writing/published_alexeymk.com
PUBLISH_BRANCH=master
set -ex

# ensure the content in /_site is up to date
cd $PUBLISH_DIR
git checkout $PUBLISH_BRANCH
rm -r * || echo "Couldn't remove"
cd -
jekyll build --destination $PUBLISH_DIR

# commit everything
cd $PUBLISH_DIR
git add .
git commit -am "$*"
git push

# come back
cd -

