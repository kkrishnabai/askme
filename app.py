from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def NamApiFnc():
    return render_template("HELLO.html")
database={}

@app.route('/'  , methods =['POST'] )
def Userdatafnd():
 if(request.form):
    btn=request.form["btn"]
    if(btn=='SIGNUP'):
        return render_template("signup.html")
    elif(btn=='LOGIN'):
        return render_template("login.html")
    elif(btn=='signup'):
        us=request.form["US"]
        pw=request.form["PW"]
        database.update({us:pw})
        return render_template("result.html",var="signup successful")
    elif(btn=='login'):
        us=request.form["US"]
        pw=request.form["PW"]
        for key,value in database.items():
            if(key==us and value==pw):
             return render_template("result.html",var="login  successful")
        else:
            return render_template("result.html",var="login  unsuccessful")
 else:      
    return render_template("HELLO.html")
            
if __name__ == '__main__':
    app.run(debug=True)
