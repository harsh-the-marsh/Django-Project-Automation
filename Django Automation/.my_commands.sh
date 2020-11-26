#!/bin/bash

function create() {
    PASSED=/e/Work/Projects/Django\ Projects$1
    #Set Your Path
    
    if [[ -z "$1" ]]; 
    then
        echo "Please Provide Project Name"
    elif [[ -z "$2" ]]; 
    then
        echo "Please Provide App Name"
    elif [ -d "${PASSED}" ]; 
    then
        echo "Your Project Is Already Exits Try Diffrent One ...!";
    else
        python create.py $1 $2
    fi
}