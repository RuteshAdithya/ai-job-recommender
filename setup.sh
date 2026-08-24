#!/bin/bash

mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = \"#7C3AED\"
backgroundColor = \"#0E1117\"
secondaryBackgroundColor = \"#161B22\"
textColor = \"#FFFFFF\"
font = \"sans serif\"

[server]
headless = true
port = \$PORT
enableCORS = false
maxUploadSize = 200

[logger]
level = \"error\"
" > ~/.streamlit/config.toml
