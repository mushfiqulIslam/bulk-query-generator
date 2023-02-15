#!/bin/bash

QUERY_PER_MINUTE="$1"
NAMESERVER="$2"
MINUTES=$3

parallel_task_count=1
if (( QUERY_PER_MINUTE > 100 )); then
  parallel_task_count=$((QUERY_PER_MINUTE/100))

  if [ $((QUERY_PER_MINUTE/100)) -gt 0 ]; then
    # round up to the next integer
    parallel_task_count=$((parallel_task_count + 1))
  fi
fi

echo "Generating $((QUERY_PER_MINUTE*MINUTES)) in $MINUTES minutes"
echo "Starting $parallel_task_count query tasks"

while [ $parallel_task_count -gt 0 ]; do
  query_number="$QUERY_PER_MINUTE"
  if [ "$QUERY_PER_MINUTE" -gt 100 ]; then
    query_number=100
    QUERY_PER_MINUTE=$((QUERY_PER_MINUTE - 100))
  fi

  python3 main.py "$query_number" "$2" "$3" &
  parallel_task_count=$((parallel_task_count - 1))
done

wait
echo "Done"
