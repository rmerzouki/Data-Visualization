mkdir -p ~/.streamlit/

echo "\
[theme]\n\
base = "dark"\n\
[server]\n\
port = $PORT\n\
enableCORS = false\n\
headless = true\n\
\n\
" > ~/.streamlit/config.toml
