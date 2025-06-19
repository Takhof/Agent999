from flask import Flask, request

app = Flask(__name__)

# メモリ上にコメント保存（再起動すると消えるよ）
comments = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        comment = request.form.get("comment", "")
        comments.append(comment)

    comment_html = "<br>".join(comments)
    return f"""
    <html>
        <head><title>Vulnerable Site</title></head>
        <body>
            <h1>コメント掲示板（超バグあり）</h1>
            <form method="POST">
                <input name="comment" />
                <input type="submit" />
            </form>
            <h2>投稿一覧</h2>
            {comment_html}
        </body>
    </html>
    """

if __name__ == "__main__":
    print("🧪 バグありWebサーバー起動中… http://localhost:5000")
    app.run(debug=True)