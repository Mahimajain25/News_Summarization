import requests
from flask import Flask,render_template,url_for
from flask import request as req
from simplet5 import SimpleT5


app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def Index():
    return render_template("index.html")

@app.route("/Summarize",methods=["GET","POST"])
def Summarize():
    if req.method== "POST":
        model = SimpleT5()
        model.load_model("t5","model\Outputs-simplet5-epoch-4-train-loss-0.6386-val-loss-1.4571")
        data=req.form["data"]
        pred = model.predict(data)
        res = pred[0]
      
        
        return render_template("index.html",result=res)
    #else:
     #   return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)