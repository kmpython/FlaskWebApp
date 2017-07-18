from flask import Flask
from flask import render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:password@localhost/FlaskRestaurantApp'
app.debug = True
db = SQLAlchemy(app)


class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    menu_item = db.relationship('MenuItem', backref="restaurant", cascade="all, delete-orphan", lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "{}".format(self.id)


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(250))
    price = db.Column(db.String(8))
    course = db.Column(db.String(250))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))

    def __init__(self, name, description, price, course, restaurant_id):
        self.name = name
        self.description = description
        self.price = price
        self.course = course
        self.restaurant_id = restaurant_id

    def __repr__(self):
        return '<MenuItem %r>' % self.name


@app.route('/')
@app.route('/restaurants/')
def showRestaurants():
    restaurants = Restaurant.query.all()
    return render_template('listRestaurants.html',  restaurants=restaurants)


@app.route('/restaurant/new', methods=['GET', 'POST'])
def postRestaurant():
    if request.method == 'POST':
        newRestaurant = Restaurant(name=request.form['name'])
        db.session.add(newRestaurant)
        db.session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('postRestaurant.html')


@app.route('/restaurant/<id>/edit', methods=['GET', 'POST'])
def editRestaurant(id):
    editRestaurant = Restaurant.query.filter_by(id=id).first()
    if request.method == 'POST' and request.form['name']:
        editRestaurant.name = request.form['name']
        db.session.commit()
        return redirect(url_for('showRestaurants'))
    else:
        return render_template('editRestaurants.html', editRestaurant=editRestaurant)


@app.route('/restaurant/<id>/delete')
def deleteRestaurant(id):
    deleteRestaurant = Restaurant.query.filter_by(id=id).first()
    db.session.delete(deleteRestaurant)
    db.session.commit()
    return redirect(url_for('showRestaurants'))


@app.route('/restaurant/<id>')
@app.route('/restaurant/<id>/menu')
def showMenu(id):
    menu = MenuItem.query.filter_by(restaurant_id=id).all()
    restaurant = Restaurant.query.filter_by(id=id).first()
    return render_template('listMenu.html', menu=menu, restaurant=restaurant)


@app.route('/restaurant/<id>/menu/new', methods=['GET', 'POST'])
def postMenu(id):
    if request.method == 'POST':
        newMenuItem = MenuItem(name=request.form['name'],
                               description=request.form['description'],
                               course=request.form['course'],
                               price=request.form['price'],
                               restaurant_id=id)
        db.session.add(newMenuItem)
        db.session.commit()
        return redirect(url_for('showMenu', id=id))
    else:
        return render_template('postMenu.html')


@app.route('/restaurant/<restaurant_id>/menu/<menu_id>/edit', methods=['GET', 'POST'])
def editMenu(restaurant_id, menu_id):
    editMenuItem = MenuItem.query.filter_by(id=menu_id).first()
    restaurantItem = Restaurant.query.filter_by(id=restaurant_id).first()
    if request.method == 'POST':
        if request.form['name']:
            editMenuItem.name = request.form['name']
        if request.form['description']:
            editMenuItem.description = request.form['description']
        if request.form['course']:
            editMenuItem.course = request.form['course']
        if request.form['price']:
            editMenuItem.price = request.form['price']
        db.session.commit()
        return redirect(url_for('showMenu', id=restaurant_id))
    else:
        return render_template('editMenu.html', editMenuItem=editMenuItem, restaurantItem=restaurantItem)


@app.route('/restaurant/<restaurant_id>/menu/<menu_id>/delete')
def deleteMenu(restaurant_id, menu_id):
    ToDeleteMenuItem = MenuItem.query.filter_by(id=menu_id).first()
    db.session.delete(ToDeleteMenuItem)
    db.session.commit()
    return redirect(url_for('showMenu', id=restaurant_id))


if __name__ == "__main__":
    app.run()