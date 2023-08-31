#!/bin/bash
# Script that takes a URL
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
