from app import db

class Staff(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    gender = db.Column(db.String(10), nullable=False)
    img_url = db.Column(db.String(500), nullable=True)
    
    
    def to_json(self):
        return {
            "id": self.id,
            "role": self.name,
            "description": self.description,
            "gender": self.gender,
            "imgUrl": self.img_url,
        }
        
        
        
        