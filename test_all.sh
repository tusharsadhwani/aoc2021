find . -maxdepth 1 -type d -name 'day_??' | xargs -i pytest {}/main.py
find . -maxdepth 1 -type d -name 'day_??' | xargs -i mypy {}/main.py