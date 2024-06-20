#!/bin/bash

# Find all PIDs related to processing-java and java
PIDS=$(ps aux | grep -E '/usr/local/bin/processing-java|/home/altar/Downloads/processing-4.3/java/bin/java' | grep -v grep | awk '{print $2}')

# Check if any PIDs were found
if [ -n "$PIDS" ]; then
    # Kill all the found processes
    echo "$PIDS" | xargs kill -9
    echo "Killed all processes related to processing-java."
else
    echo "No processes found running processing-java."
fi
