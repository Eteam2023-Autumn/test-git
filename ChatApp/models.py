import pymysql
from util.DB import DB

#ユーザー登録機能
#データーベースへのユーザー登録のための関数
class dbConnect:
    def createUser(uid, name, email, password):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);"
            cur.execute(sql, (uid, name, email, password))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}") #例外の文字列表現を取得
            abort(500)
        finally:
            cur.close()


#ログイン機能(認証機能)
#ユーザー情報を取り出す
    def getUser(email):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM users WHERE email=%s;"
            cur.execute(sql, (email,))#emailをタプルとして渡す
            user = cur.fetchone()
            return user
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


#チャンネル一覧機能
    def getChannelAll():
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels;"
            cur.execute(sql)
            channels = cur.fetchall()
            return channels
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()     


#チャンネル作成機能
    def getChannelById(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid,))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()         


    def getChannelByName(channel_name):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE name=%s;"
            cur.execute(sql, (channel_name,))
            channel = cur.fetchone()
            return channel
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


    def addChannel(uid, newChannelName, newChannelDescription):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);"
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


#チャンネル編集機能
    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
            cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()     


#deleteチャンネル関数
    def deleteChannel(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid,))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


#メッセージ作成機能
#アプリ唯一の内部結合を利用
    def getMessageAll(cid):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT id,u.uid, user_name,department message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"#departmentのデータも追加で取得
            cur.execute(sql, (cid,))
            messages = cur.fetchall()
            return messages
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


#データーベースにメッセージを登録している
    def createMessage(uid, cid, message):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)"
            cur.execute(sql, (uid, cid, message))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()


#メッセージ削除機能
    def deleteMessage(message_id):
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM messages WHERE id=%s;"
            cur.execute(sql, (message_id,))
            conn.commit()
        except Exception as e:
            print(f"エラーが発生しました: {str(e)}")
            abort(500)
        finally:
            cur.close()               