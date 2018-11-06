git add .
git commit -m "commit"

git push heroku master

heroku run python line_bitcoin.py

git submodule add git://github.com/Grawor/common_python.git common_python
git submodule add git://github.com/Grawor/fcoin-python-sdk.git fcoin-python-sdk