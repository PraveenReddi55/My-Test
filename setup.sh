mkdir -p~/.streamlit/

echo "
[server]\n
headless = true\n
enableCORS=fasle\n
port = $port\n
" > ~/.streamlit/config.toml
