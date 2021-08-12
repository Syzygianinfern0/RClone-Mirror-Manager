#!/bin/bash

drives=(
    "test"
    "one"
    "two"
    "three"
    "four"
    "five"
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
    rclone --config rclone.conf sync --drive-server-side-across-configs "$from": "$to":sync/"$from"
done

from="${mirrors[1]}"
for to in "${mirrors[@]:1}"; do
    echo "$from"
    echo "$to"
    rclone --config rclone.conf sync --drive-server-side-across-configs "$from":sync/ "$to":sync/
done
