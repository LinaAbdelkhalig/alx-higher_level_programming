#!/bin/bash
# displays the status code only
curl -s -o /dev/null -w "%{https_code}" "$1"
