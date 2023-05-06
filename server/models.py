from app import db

class Image(db.Model):

    __tablename__="images"

    id=db.Column(db.Integer,primary_key="True")
    description=db.Column(db.String)
    image=db.Column(db.Blob)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_onupdate=db.func.now())

