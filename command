# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# 手順関連
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

---- 初めてgitでコミットする場合 ----
git init

※GithubのCloud9用SSHキー登録が未実施であれば登録する。

---- リモートGitを登録する場合 ----
1. 登録されているリモートGitを確認）
git remote -v

2. git のリモート登録＜git remote add [shortname] [url]＞
git remote add origin git@github.com:Grawor/auto_bot.git

---- 更新したファイル類をリモートGitにアップデートする場合 ----
git add .
git commit -m "commit"
git push origin master

※origin:登録したリモートリポジトリのショートネーム master:このリポジトリ
※Git push でエラーが発生時は強制マージを試してみる。

---- モジュールをインストール（追加）したことをHerokuへ反映させる場合 ----
1. requirements.txt と Pipfile と Pipfile.lock ファイルを削除
2. requirements.txt ファイルを更新
pip freeze > requirements.txt
3. pipenv install を実施
pipenv install

---- プログラムファイル更新時 Heroku へのデプロイ ----
1. git コミット
git add .
git commit -m "commit"
2. Heroku へプッシュ
git push heroku master
3. Heroku側でPythonファイルが起動するかテスト
heroku run python auto_bot.py

---- git サブモジュール追加方法（初めて作成する場合） ----
git submodule add git://github.com/Grawor/common_python.git common_python
git submodule add git://github.com/Grawor/fcoin-pythsudon-sdk.git fcoin-python-sdk

---- git サブモジュール追加方法（一度サブモジュールを作成してしまっていた場合） ----
git submodule add --force git://github.com/Grawor/common_python.git common_python
git submodule add --force git://github.com/Grawor/fcoin-python-sdk.git fcoin-python-sdk

---- git サブモジュール更新 ----
git submodule foreach git pull origin master

---- anaconda のインストール ----
git clone https://github.com/yyuu/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
source ~/.bashrc
pyenv install anaconda3-4.0.0
pyenv rehash
pyenv global anaconda3-4.0.0

---- jupyter notebook を起動 ----
jupyter notebook --ip 0.0.0.0 --port 8080 --no-browser


# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
# コマンドのメモ
# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----

---- pythonファイルの実行
---- 【注意】pythonで実行だとpython2のシステムパスを参照するためモジュールが見つからないエラーとなる。
python3 line_bitcoin.py    

---- 登録しているgitの確認
git remote -v

---- git のリモートurlを変更
git remote set-url origin {new url}
git remote set-url origin git@github.com:Grawor/auto_bot.git

---- git リモートにpush時に! [rejected] master -> master (fetch first)エラーの場合
git fetch
git merge origin/master
git push origin master
※NG:git merge --allow-unrelated-histories origin/master

---- Heroku に環境変数を設定　※一度設定されれば、再度デプロイしても残っている
heroku config:set 環境変数名称1=設定したいkey1 環境変数名称2=設定したいkey2 

---- Heroku の環境変数を確認
heroku config:get 環境変数

---- ヴァージョン確認
python -m pip list
python3 --version // python3のversion確認

---- パッケージのインストール（sudo:管理者権限で実行【重要】）
sudo pip install numpy
sudo pip install --upgrade pip

---- sudo pip が動作しない（pip と sudo のディレクトリが異なる）場合
sudo cp /usr/local/bin/pip /usr/bin/
