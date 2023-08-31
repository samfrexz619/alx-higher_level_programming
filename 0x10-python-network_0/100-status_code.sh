#!/bin/bash
# Script that sends req to a URL passed as an arg
curl -so /dev/null -w "%{http_code}" "$1"
