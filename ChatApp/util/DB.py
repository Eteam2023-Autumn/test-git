import pymysql

class DB:
<<<<<<< HEAD
    def getConnection():#getConnection()：データベースへの接続に使用されたユーザー名およびパスワードと関連付けられている接続を戻す
=======
    def getConnection():
>>>>>>> 9da3d3c8262176ccad8ca15b7812fb81d913b943
        try:
            conn = pymysql.connect(
            host="db",
            db="chatapp",
            user="testuser",
            password="testuser",
            charset="utf8",
            cursorclass=pymysql.cursors.DictCursor
<<<<<<< HEAD
        )#pymysqlに接続するための認証情報を設定して、pymysqlに接続している
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()#con.close:pymysqlの接続を終了している
=======
        )
            return conn
        except (ConnectionError):
            print("コネクションエラーです")
            conn.close()
>>>>>>> 9da3d3c8262176ccad8ca15b7812fb81d913b943
