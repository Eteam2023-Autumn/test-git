from flask import Flask, app, request, redirect, render_template, session, flash, abort
from datetime import timedelta
import uuid
import re

from models import dbConnect
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = uuid.uuid4().hex 
app.permanent_session_lifetime = timedelta(days=30)
bcrypt = Bcrypt(app)

# サインアップページの表示
@app.route("/signup", methods=["GET"])
def signup():
    return render_template('registration/signup.html')


# サインアップ処理
@app.route('/signup', methods=['POST'])
def userSignup():
    name = request.form.get('name')
    email = request.form.get('email')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
   

    pattern = "^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

    # 予め文字列として保存する
    uid = str(uuid.uuid4())

    if name == '' or email =='' or password1 == '' or password2 == '':
        flash('空のフォームがあるようです')
    elif password1 != password2:
        flash('パスワードが一致しません。')
    # not re.は True を返す
    elif not re.match(pattern, email): 
        flash('正しいメールアドレスの形式ではありません')
    else:
        if dbConnect.getUser(email) is not None:
            flash('既に登録されているメールアドレスです')
        
        else:
        # パスワードのハッシュ化、ユーザー登録手続き
            password_hash = bcrypt.generate_password_hash(password1).decode('utf-8')    
            dbConnect.createUser(uid, name, email, password_hash) 
            session['uid'] = uid

            return redirect('/')
        
    return redirect('/signup')


# ログインページの表示
@app.route('/login')
def login():
    return render_template('registration/login.html')


# ログイン処理
@app.route('/login', methods=['POST'])
def userLogin():
    email = request.form.get('email')
    password = request.form.get('password')

    if email =='' or password == '':
        flash('空のフォームがあります。')
    else:
        user = dbConnect.getUser(email)
        if user is None:
            flash('このユーザーは存在しません')
        else:
            #パスワードの検証
            if not bcrypt.check_password_hash(user["password"], password):
                flash('パスワードが間違っています！')
            else:
                session['uid'] = user["uid"]
                return redirect('/')
            
    return redirect('/login')


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
    
    # 入力されたチャンネル名が既にDBに存在するか確認
    channel_name = request.form.get('channelTitle')
    existing_channel = dbConnect.getChannelByName(channel_name)

    # 同名のチャンネルが存在しない場合にのみ追加
    if existing_channel is None:
        channel_description = request.form.get('channelDescription')
        dbConnect.addChannel(uid, channel_name, channel_description)
        return redirect('/')
    
    else:
        error_message = '既に同じ名前のチャンネルが存在しています'
        return render_template('error/error.html', error_message=error_message)


# チャンネルの更新
@app.route('/update_channel', methods=['POST'])
def update_channel():
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
 
    
    # フォームからチャンネルID、タイトル、説明を取得しチャンネル更新
    cid = request.form.get('cid')
    channel_name = request.form.get('channelTitle')
    channel_description = request.form.get('channelDescription')
    dbConnect.updateChannel(uid, channel_name, channel_description, cid)

    return redirect('/detail/{cid}'.format(cid=cid))


# チャンネルの削除
@app.route('/delete/<cid>')
def delete_channel(cid):
    uid = session.get("uid")
    if uid is None:
        return redirect('/login')
    
    # DBからチャンネル情報を取得
    channel = dbConnect.getChannelById(cid)
    
    # 削除者=作成者の場合にのみ削除
    if channel["uid"] == uid:
        dbConnect.deleteChannel(cid)
        channels = dbConnect.getChannelAll()
    else:
        flash('チャンネルは作成者のみ削除可能です')

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

#@app.errorhandler(404)
#def show_error404(error):
   # return render_template('error/404.html'),404


#@app.errorhandler(500)
#def show_error500(error):
    #return render_template('error/500.html'),500

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False)
