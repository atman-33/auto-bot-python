------ 手順関連 ------

// モジュールをインストール（追加）したことをHerokuへ反映させる場合
①requirements.txt ファイルを更新
②Pipfile と Pipfile.lock ファイルを削除
③pipenv install を実施

// プログラムファイル更新時 Heroku へのデプロイ
①git コミット
②Heroku へプッシュ

------ コマンド関連 ------

// pythonファイルの実行
python3 line_bitcoin.py    // 【注意】pythonで実行だとpython2のシステムパスを参照するためモジュールが見つからないエラーとなる。

// 登録しているgitの確認
git remote -v

// git コミット
git add .
git commit -m "commit"

// git リポジトリ（リモート）へプッシュ origin:このリポジトリ maste:リモートリポジトリ
git push origin master

// git のリモートurlを変更
git remote set-url origin {new url}
git remote set-url origin https://github.com/Grawor/auto_bot.git

// git リモートにpush時に! [rejected] master -> master (fetch first)エラーの場合
git merge --allow-unrelated-histories origin/master

// Heroku へプッシュ（デプロイ）
git push heroku master

// Heroku に環境変数を設定　※一度設定されれば、再度デプロイしても残っている
heroku config:set 環境変数名称1=設定したいkey1 環境変数名称2=設定したいkey2 

// Heroku の環境変数を確認
heroku config:get 環境変数

// Heroku で python ファイルを起動
heroku run python line_bitcoin.py

// git サブモジュール追加方法（初めて作成する場合）
git submodule add git://github.com/Grawor/common_python.git common_python
git submodule add git://github.com/Grawor/fcoin-pythsudon-sdk.git fcoin-python-sdk

// git サブモジュール追加方法（一度サブモジュールを作成してしまっていた場合）
git submodule add --force git://github.com/Grawor/common_python.git common_python
git submodule add --force git://github.com/Grawor/fcoin-python-sdk.git fcoin-python-sdk

// git サブモジュール更新
git submodule foreach git pull origin master

// ヴァージョン確認
python -m pip list
python3 --version // python3のversion確認

// パッケージのインストール（sudo:管理者権限で実行【重要】）
sudo pip install numpy
sudo pip install --upgrade pip

// sudo pip が動作しない（pip と sudo のディレクトリが異なる）場合
sudo cp /usr/local/bin/pip /usr/bin/

// requirements.txt, pipfileの作成
pip freeze > requirements.txt
pipenv install