#!/bin/bash

# Testing purpose only
export FLASK_ENV=development
gunicorn -w 4 -b 127.0.0.1:5000 'app:create_app()'