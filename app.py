from flask import Flask, render_template, request,redirect,url_for
import raffle

app = Flask(__name__)
users = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        if any(user['email'] == email for user in users):
            return render_template('index.html', users=users, error='Email address must be unique.')
        users.append({'username': username, 'email': email})
    return render_template('index.html', users=users)



@app.route('/calculate_presents')
def calculate_presents():
    raffle.raffle(users)
    users.clear()
    return redirect("/")

@app.route('/remove_user', methods=['GET'])
def remove_user():
    email_to_remove = request.args.get('email')
    if email_to_remove:
        users[:] = [user for user in users if user['email'] != email_to_remove]
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
