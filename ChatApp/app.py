from flask import Flask, request, render_template, redirect, session, flash
from datetime import timedelta
from passlib.hash import bcrypt
import secrets 
import re
import uuid
from models import dbConnect
import hashlib

app = Flask(__name__)
app.secret_key = secrets.token_hex(32)
app.permanent_session_lifetime = timedelta(days=30)


#サインアップのページ
@app.route("/signup", methods=["GET"])
def signup():
    if request.method == "GET":
        return render_template('registration/signup.html')


#サインアップの処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')

    email_pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    if not all([name,email,password1,password2]):
        flash('すべてのフォームを入力してください。')
    elif password1 != password2:
        flash('パスワードが一致しません。')
    elif not re.match(email_pattern,email):
        flash('正しいメールアドレスの形式ではありません。')
    else:
        if dbConnect.getUser(email) is not None:
            flash('既に登録されているメールアドレスです')
        else:
            uid = uuid.uuid4()
            password = hashlib.sha256(password1.encode('utf-8')).hexdigest()

            dbConnect.createUser(uid, name, email, password)
            UserId = str(uid)
            session['uid'] = str(uid)
            return redirect('/')
    #エラー時にサインアップページにリダイレクト    
    return redirect('/signup')


#ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')

#ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == '' or password == '':
        flash('空のフォームがあります。')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません。')
        else:
            hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
            
            if hashed_password != user["password"]:
                flash('パスワードが間違っています！')
            else:
                session['uid'] = str(user["uid"])
                
                return redirect('/')

    return redirect('/login')

<<<<<<< Updated upstream:ChatApp/app.py
<<<<<<< Updated upstream:ChatApp/app.py

# ログアウト
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')


# チャンネル一覧ページの表示
@app.route('/')
def index():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channels = dbConnect.getChannelAll()
        channels.reverse()
    return render_template('index.html', channels=channels, uid=uid)


# チャンネルの追加
@app.route('/', methods=['POST'])
def add_channel():
    uid = session.get('uid')
    if uid is None:
        return redirect('/login')
    channel_name = request.form.get('channelTitle')
    channel = dbConnect.getChannelByName(channel_name)
    if channel == None:
        channel_description = request.form.get('channelDescription')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    else:
        error = '既に同じ名前のチャンネルが存在しています'
        return render_template('error/error.html', error_message=error)


# チャンネルの更新
@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = request.form.get('cid')
    channel_name = request.form.get('channelTitle')
    channel_description = request.form.get('channelDescription')

    dbConnect.updateChannel(uid, channel_name, channel_description, cid)
    return redirect('/detail/{cid}'.format(cid = cid))


# チャンネルの削除
@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    else:
        channel = dbConnect.getChannelById(cid)
        if channel["uid"] != uid:
            flash('チャンネルは作成者のみ削除可能です')
            return redirect ('/')
        else:
            dbConnect.deleteChannel(cid)
            channels = dbConnect.getChannelAll()
            return redirect('/')


# チャンネル詳細ページの表示
@app.route('/detail/<cid>')
def detail(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    cid = cid
    channel = dbConnect.getChannelById(cid)
    messages = dbConnect.getMessageAll(cid)

    return render_template('detail.html', messages=messages, channel=channel, uid=uid)


# メッセージの投稿
@app.route('/message', methods=['POST'])
def add_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message = request.form.get('message')
    cid = request.form.get('cid')

    if message:
        dbConnect.createMessage(uid, cid, message)

    return redirect('/detail/{cid}'.format(cid = cid))


# メッセージの削除
@app.route('/delete_message', methods=['POST'])
def delete_message():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')

    message_id = request.form.get('message_id')
    cid = request.form.get('cid')

    if message_id:
        dbConnect.deleteMessage(message_id)

    return redirect('/detail/{cid}'.format(cid = cid))


# @app.errorhandler(404)
# def show_error404(error):
#     return render_template('error/404.html'),404


# @app.errorhandler(500)
# def show_error500(error):
#     return render_template('error/500.html'),500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
=======
#ログアウト
>>>>>>> Stashed changes:ChatApp/util/app.py
=======
#ログアウト
>>>>>>> Stashed changes:ChatApp/util/app.py
