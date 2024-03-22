from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@Dretliee13865557@",
    database="test"
)
cursor = db.cursor()

# Routes for CRUD Operations
@app.route('/')
def home():
    cursor.execute("SELECT * FROM messages")
    data = cursor.fetchall()
    return render_template('index.html', data=data)

@app.route('/create', methods=['POST'])
def create():
    fname = request.form['fname']
    city = request.form['city']
    country = request.form['country']
    cursor.execute("INSERT INTO messages (fname, city, country) VALUES (%s, %s, %s)", (fname, city, country))
    db.commit()
    return redirect(url_for('home'))

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    fname = request.form['fname']
    city = request.form['city']
    country = request.form['country']
    cursor.execute("UPDATE messages SET fname = %s, city = %s, country = %s WHERE id = %s", (fname, city, country, id))
    db.commit()
    return redirect(url_for('home'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor.execute("DELETE FROM messages WHERE id = %s", (id,))
    db.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
