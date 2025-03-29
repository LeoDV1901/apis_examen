from config import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False) 
    last_name = db.Column(db.String(100))
    

    def __init__(self, name, email, password, last_name=None):
        self.name = name
        self.email = email
        self.password = password
        self.last_name = last_name

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password':self.password,
            'last_name': self.last_name
            
        }
