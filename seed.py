from app import app
from models import db, User

with app.app_context():
    print("Seeding user data")
    db.session.add(User(username="Felix", age="200"))
    db.session.add(User(username="Ivy", age="2"))
    db.session.add(User(username="Brighton", age="20"))
    db.session.add(User(username="Brenda", age="30"))
    db.session.add(User(username="Chelsea", age="70"))
    # db.create_all()

    # users = [
    #     User(username='XXXXX', password='XXXXXXXXX'),
    #     User(username='XXXXX', password='XXXXXXXXX'),
    #     User(username='XXXXX', password='XXXXXXXXX')
    # ]

    # db.session.add_all(users)
    db.session.commit()
    print("done seeding")
