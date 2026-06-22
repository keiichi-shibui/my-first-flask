from flask import Flask

# FlaskのWebサーバーを起動する準備
app = Flask(__name__)

# インターネットで「/」（トップページ）にアクセスされた時の処理
@app.route("/")
def home():
    # ブラウザに表示する文字（HTML）
    return """
    <html>
        <head>
            <title>Flask体験アプリ</title>
        </head>
        <body style="text-align: center; font-family: sans-serif; padding-top: 50px;">
            <h1>こんにちは！これはあなたが作ったWebサイトです！</h1>
            <p>Flaskを使えば、このようなページをPythonから瞬時に作れます。</p>
            <p style="color: gray;">（VS Codeのターミナルにある URL をクリックしてみてね）</p>
        </body>
    </html>
    """

if __name__ == "__main__":
    # デバッグモード（コードを書き換えると自動でページが更新されるモード）で起動
    app.run(debug=True)