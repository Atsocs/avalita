#!/bin/bash
export COMPOSE_PROJECT_NAME=avalita_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run avalita unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
