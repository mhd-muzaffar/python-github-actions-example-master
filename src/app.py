from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
<<<<<<< HEAD
    return "Hello,IT world!"
=======
    return "Hello,NSC123 world!"
>>>>>>> 20a03b6c1dd3c43e868d5a8fe5692b656714cf5f


if __name__ == "__main__":
    app.run()

