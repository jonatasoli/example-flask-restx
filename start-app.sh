#!/bin/bash

# Start Gunicorn
gunicorn -w 1 -b 0.0.0.0:5000 --threads 1 app:app --access-logfile /src/logs --error-logfile /src/logs
