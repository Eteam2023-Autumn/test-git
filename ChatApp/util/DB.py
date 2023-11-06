import pymysql

class DB:
    def getConnection():#getConnection()：データベースへの接続に使用されたユーザー名およびパスワードと関連付けられている接続を戻す
        try:
            conn = pymysql.connect(
            host="db",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
        )#pymysqlに接続するための認証情報を設定して、pymysqlに接続している
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()#con.close:pymysqlの接続を終了している
