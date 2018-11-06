// git コミット
git add .
git commit -m "commit"

// git レポジトリ（リモート）へプッシュ
git push origin master

// Heroku へプッシュ（デプロイ）
git push heroku master

// Heroku で python ファイルを起動
heroku run python line_bitcoin.py

// git サブモジュール追加方法
git submodule add git://github.com/Grawor/common_python.git common_python
git submodule add git://github.com/Grawor/fcoin-python-sdk.git fcoin-python-sdk

// git サブモジュール追加方法（一度サブモジュールを作成してしまっていた場合）
git submodule add --force git://github.com/Grawor/common_python.git common_python
git submodule add --force git://github.com/Grawor/fcoin-python-sdk.git fcoin-python-sdk

// ヴァージョン確認
python -m pip list

// パッケージのインストール（sudo:管理者権限で実行【重要】）
sudo pip install numpy
sudo pip install --upgrade pip