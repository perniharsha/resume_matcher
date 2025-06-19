#!/bin/bash

uvicorn app_api.main:app --host 0.0.0.0 --port 8000 &
streamlit run front_end/app.py --server.port 8501 --server.address 0.0.0.0

