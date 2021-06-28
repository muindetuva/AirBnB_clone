#!/usr/bin/env bash

echo "# This file lists all individuals having contributed content to the repository." > AUTHORS
echo "" >> AUTHORS
git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf >> AUTHORS
