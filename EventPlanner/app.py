from flask import Flask
app = Flask(__name__)
params = ['Ayaan','Einstein']
@app.route('/')
def home():
    return render_template('index.html')
 
@app.route('/login')
def login():
    if 'user' in session and session['user'] in params['admin_user']:       # checking if user is already in session
        posts = my_posts.query.all()
        return render_template('dashboard.html', params=params, posts=posts)

    if request.method == 'POST':
        username = request.form.get("uname")
        userpass = request.form.get("upass")
        if username in params['admin_user'] and userpass == params['admin_password']:       # validating the login info
            session['user'] = username      # adding user into the session
            posts = my_posts.query.all()
            return render_template('dashboard.html', params=params, posts=posts)
        else:
            return redirect('/dashboard')   # redirecting back to login page if login fails
    else:
        return render_template("login.html", params=params)

if __name__ == '__main__':
    app.run()
