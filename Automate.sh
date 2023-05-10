#!/bin/bash

echo "Hi Boss Innocent Charles, kindly Enter your commit message"
read message


git add .
git commit -m "$message"
git push
