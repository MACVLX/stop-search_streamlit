mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
[theme]
primaryColor=#A8DBA8
backgroundColor=#E0E4CC
secondaryBackgroundColor=#3B8686
textColor=#262730
font=sans serif
" > .streamlit/config.toml