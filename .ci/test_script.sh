#!/bin/bash

# Be verbose, and stop with error as soon there's one
set -ev

case "$TEST_TYPE" in
    test)
        # Run the AiiDA tests
        cd ${TRAVIS_BUILD_DIR}/tests; pytest
        ;;
    precommit)
        pre-commit run --all-files
        ;;
esac
