#!/bin/bash
PORT=${PORT:-8501}
streamlit run front_end/app.py --server.port=$PORT --server.address=0.0.0.0
