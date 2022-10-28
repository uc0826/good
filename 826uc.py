from flask import Flask,render_template

app = Flask(__name__)


@app.route("/")
def index():
    homepage = "<h1>主頁</h1>"
    homepage += "<a href=/aboutnutty>MIS個人介紹</a><br><br>"
    homepage += "<a href=/hobby>我的興趣</a><br><br>"
    homepage += "<a href=/job>職業</a><br><br>"
    homepage += "<a href=/plan>未來的計劃</a><br><br>"
    return homepage


@app.route("/aboutnutty")
def aboutnutty(): 
    return render_template ("aboutnutty.html")

@app.route("/hobby")
def hobby(): 
   return render_template("hobby.html")

@app.route("/job")
def job(): 
   return render_template("job.html")

@app.route("/plan")
def plan(): 
   return render_template("plan.html")


#if __name__ == "__main__":
#    app.run()