#!/bin/bash
# send request to URL to display size of response
curl -so /dev/null -w '%{size_download}\n' $1
