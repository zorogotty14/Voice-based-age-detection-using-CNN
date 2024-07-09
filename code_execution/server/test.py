from flask import Flask,render_template,request,session,redirect,url_for

app =Flask(__name__)


@app.route("/upload")
def upload():
    list_songs = [["abc", "Undo","abc"],["abc","Fireflies","xy"],["abc", "Undo","abc"],["abc","Fireflies","xy"]]
    return render_template('home.html',list_of_songs=list_songs)

if __name__=='__main__':
    app.run(debug=True,port=5000,host="0.0.0.0")
