#!/bin/bash

STATUS=$(curl –write-out “%{http_code}n” –silent –output /dev/null "your_url")

if [[ STATUS -eq 200 ]]; then
echo “Success”
else
echo “Failed”
fi