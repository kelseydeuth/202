#!/bin/bash

git add -A && git commit -am "automated upload" && git push
ssh calpoly "cd 202; git fetch --all; git reset --hard origin/master"

