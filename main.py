from flaskr import app
from flask import render_template, request, redirect, url_for
import sqlite3

DATABASE = 'database.db'

@app.route('/')
def index():
    con = sqlite3.connect(DATABASE)
    db_Cars = con.execute('SELECT * FROM Cars').fetchall()
    con.close()

    Cars = []
    for row in db_Cars:
        Cars.append({
            'Registration Number': row[0], 
            'Brand': row[1], 
            'Model': row[2], 
            'Color': row[3], 
            'Contact Information': row[4], 
            'Vehicle ID Number': row[5]
        })
    return render_template('index.html', Cars=Cars)


@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/register', methods=['POST'])
def register():
    brand = request.form['Brand']
    model = request.form['Model']
    color = request.form['Color']
    contact_info = request.form['Contact Information']
    vehicle_ID_num = request.form['Vehicle ID Number']

    con = sqlite3.connect(DATABASE)
    con.execute('''
    INSERT INTO Cars (Brand, Model, Color, "Contact Information", "Vehicle ID Number")
    VALUES (?, ?, ?, ?, ?)
    ''', [brand, model, color, contact_info, vehicle_ID_num])

    con.commit()
    con.close()
    return redirect(url_for('index'))


@app.route('/delete', methods=['POST'])
def delete():
    registration_num = request.form['Registration Number']

    con = sqlite3.connect(DATABASE)
    con.execute('DELETE FROM Cars WHERE "Registration Number" = ?', [registration_num])
    con.commit()
    con.close()
    return redirect(url_for('index'))