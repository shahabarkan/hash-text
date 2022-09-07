import hashlib
from flask import *

app = Flask(__name__)

@app.route("/code", methods=["GET","POST"])
def coding():
    try:
        data_n = request.json["text"]
        tobit = bytes(data_n,"UTF-8")
        m = hashlib.md5(tobit)
        return m.hexdigest()
    except Exception as e:
        d = {"stastus_code":400,
             "msg":str(e)}
        return d

app.run(debug=True)