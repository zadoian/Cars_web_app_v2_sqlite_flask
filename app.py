from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database connection
def get_db_connection():
    conn = sqlite3.connect('cars.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

# View all cars
@app.route('/cars')
def view_cars():
    conn = get_db_connection()
    cars = conn.execute('SELECT * FROM Cars').fetchall()
    conn.close()
    return render_template('cars.html', cars=cars)

# Add a new customer and car
@app.route('/add_customer', methods=['GET', 'POST'])
def add_customer():
    if request.method == 'POST':
        customer = request.form['customer']
        color = request.form['color']
        brand = request.form['brand']
        conn = get_db_connection()
        conn.execute('INSERT INTO Cars (Customer, Color, Brand) VALUES (?, ?, ?)', (customer, color, brand))
        conn.commit()
        conn.close()
        return redirect(url_for('view_cars'))
    return render_template('add_customer.html')

# Edit car details
@app.route('/edit_car/<int:id>', methods=['GET', 'POST'])
def edit_car(id):
    conn = get_db_connection()
    car = conn.execute('SELECT * FROM Cars WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        new_color = request.form['color']
        new_brand = request.form['brand']
        conn.execute('UPDATE Cars SET Color = ?, Brand = ? WHERE id = ?', (new_color, new_brand, id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_cars'))

    return render_template('edit_car.html', car=car)

# Search for cars
@app.route('/search_car', methods=['GET', 'POST'])
def search_car():
    if request.method == 'POST':
        customer = request.form['customer']
        color = request.form['color']
        brand = request.form['brand']
        
        conn = get_db_connection()
        cars = conn.execute('SELECT * FROM Cars WHERE Customer=? AND Color=? AND Brand=?',
                            (customer, color, brand)).fetchall()
        conn.close()

        return render_template('search_results.html', cars=cars)
    
    return render_template('search_car.html')

# Delete car
@app.route('/delete_car/<int:id>', methods=['GET', 'POST'])
def delete_car(id):
    conn = get_db_connection()
    if request.method == 'POST':
        conn.execute('DELETE FROM Cars WHERE id = ?', (id,))
        conn.commit()
        conn.close()
        return redirect(url_for('view_cars'))
    
    car = conn.execute('SELECT * FROM Cars WHERE id = ?', (id,)).fetchone()
    conn.close()
    return render_template('delete_car.html', car=car)

if __name__ == '__main__':
    app.run(debug=True)
