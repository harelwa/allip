#!/bin/bash

while true; do
    task voices:night:play:quasi-still
    sleep ${SLEEP_AFTER_QUASI}
    task voices:night:play:quasi-still
    sleep ${SLEEP_AFTER_QUASI}
    task voices:night:play:quasi-still
    sleep ${SLEEP_AFTER_QUASI}
    task voices:night:play:cello-no-two-bi-cluster
    sleep ${SLEEP_AFTER_BI_CLUSTER}
done
