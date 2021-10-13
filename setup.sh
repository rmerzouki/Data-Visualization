mkdir -p ~/.streamlit/

echo "[theme]
primaryColor = "#f63366"
backgroundColor = "#0e1117"
secondaryBackgroundColor = "#31333F"
textColor = "#fafafa"
font = "sans serif"
[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
