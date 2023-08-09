#!/bin/bash
mkdir -p runtime/logs/

CONSOLE_LOG="runtime/logs/smartest_manager_console_`date +%Y%m%d`.log"

echo $CONSOLE_LOG

nohup ./smartest-manager >> $CONSOLE_LOG 2>&1 &