#!/bin/bash

echo "Please enter a ip address"
read  input

echo "Please provide an wordlist"
read  -e  wordlist

nikto -h http://$input

python3 dirsearch.py http://$input $wordlist
