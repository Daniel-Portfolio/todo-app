#!/bin/bash

BASE_URL="http://0.0.0.0:5000/api/todos"

POST_DATA='{
  "title": "test",
  "description": "test",
  "completed": false
}'

echo "Performing POST request..."
curl -s -X POST -H "Content-Type: application/json" -d "$POST_DATA" "$BASE_URL"

echo "Performing GET request..."
curl -s -X GET "$BASE_URL"