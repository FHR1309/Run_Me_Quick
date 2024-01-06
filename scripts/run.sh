#!/bin/bash
source venv/bin/activate
cd src
uvicorn start:app --reload
