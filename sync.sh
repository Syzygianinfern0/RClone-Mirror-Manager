#!/bin/bash

drives=(
    "test"
)

mirrors=(
    "1"
    "2"
    "3"
    "4"
    "5"
)

to="${mirrors[1]}"
for from in "${drives[@]}"; do
    echo "$from"
    echo "$to"
    rclone --config rclone.conf -P sync --drive-server-side-across-configs "$from": "$to":sync/"$from"
done

from="${mirrors[1]}"
for to in "${mirrors[@]:1}"; do
    echo "$from"
    echo "$to"
    rclone --config rclone.conf -P sync --drive-server-side-across-configs "$from":sync/ "$to":sync/
done
