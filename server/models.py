from config import db
from sqlalchemy_serializer import SerializerMixin

class Image(db.Model,SerializerMixin):

    __tablename__="images"

    id=db.Column(db.Integer,primary_key="True")
    description=db.Column(db.String)
    image=db.Column(db.LargeBinary)
    created_at=db.Column(db.DateTime,server_default=db.func.now())
    updated_at=db.Column(db.DateTime,server_onupdate=db.func.now())

