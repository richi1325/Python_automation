#!/bin/bash

line="-------------------------"
echo "Starting at: $(date)"; echo
echo $line
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"
fi
echo $line
echo "Finishing at: $(date)"