mkdir -p ~/.streamlit/
echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml


# [theme]\n\
# primaryColor=#A8DBA8\n\
# backgroundColor=#E0E4CC\n\
# secondaryBackgroundColor=#3B8686\n\
# textColor=#262730\n\
# font=sans serif\n\