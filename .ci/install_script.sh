#!/bin/bash

# Author: Dominik Gresch <greschd@gmx.ch>

# Be verbose, and stop with error as soon there's one
set -ev

pip install -U 'pip<19' wheel setuptools

cd ${TRAVIS_BUILD_DIR}

case "$INSTALL_TYPE" in
    test_pypi)
        pip install --pre fsc.export[test]
        ;;
    test_sdist)
        python setup.py sdist
        ls -1 dist/ | xargs -I % pip install dist/%[test]
        ;;
    test)
        pip install .[test]
        ;;
    precommit)
        pip install .[precommit]
        ;;
esac
