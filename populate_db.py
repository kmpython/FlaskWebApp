from app import db, Restaurant, MenuItem

restaurant1 = Restaurant(name="Urban Burger")
db.session.add(restaurant1)
db.session.commit()

menuItem1 = MenuItem(name="Veggie Burger", description="Juicy grilled veggie patty with tomato mayo and lettuce",
                      price="$7.50", course="Entree", restaurant_id=restaurant1.id)
db.session.add(menuItem1)

menuItem2 = MenuItem(name="Chicken Burger", description="Juicy grilled chicken patty with tomato mayo and lettuce",
                      price="$5.50", course="Entree", restaurant_id=restaurant1.id)
db.session.add(menuItem2)

menuItem3 = MenuItem(name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant_id=restaurant1.id)
db.session.add(menuItem3)
db.session.commit()

restaurant2 = Restaurant(name="Super Stir Fry")
db.session.add(restaurant2)
db.session.commit()

menuItem4 = MenuItem(name="Nepali Momo ", description="Steamed dumplings made with vegetables, spices and meat. ",
                     price="12", course="Entree", restaurant_id=restaurant2.id)
db.session.add(menuItem4)

menuItem5 = MenuItem(name="Beef Noodle Soup", description="A Chinese noodle soup made of stewed or red braised beef, beef broth, vegetables and Chinese noodles.",
                     price="14", course="Entree", restaurant_id=restaurant2.id)
db.session.add(menuItem5)
db.session.commit()