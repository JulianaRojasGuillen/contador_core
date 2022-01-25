from flask import Flask,render_template,request,redirect,session

app = Flask(__name__)
app.secret_key = "estoessecreto"

@app.route ('/', methods=['GET'])
def despliegaInicio():
    if "contador" not in session:
      session["contador"] = 1
    else:
        session["contador"] += 1

    return render_template("index.html")

@app.route ('/incrementar', methods=['GET'])
def incrementaenDos():
    session['contador']+=1
    return redirect('/')

@app.route ('/resetear',methods=['GET'])
def resetearContador():
    session.clear()
    return redirect ('/')

if __name__ == "__main__":
    app.run(debug=True)

