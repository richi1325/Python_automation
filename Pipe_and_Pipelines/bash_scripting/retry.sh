#!/bin/bash

n=0
command=$1 #Primer argumento en la linea de comandos
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n+1))
    echo "Retry: #$n"
done;