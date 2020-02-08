from Extensions.Database import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, default=None)
    city = db.Column(db.String(3), default=None)

    def asdict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "age": self.age,
            "city": self.city
        }

    def save(self):
        """Saves the user to the db"""
        if self.id is None:
            db.session.add(self)
        return db.session.commit()
