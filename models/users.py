from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()
class Users(db.model):
    __tablename__="users"
    id=db.Column(db.Integer,Primary_Key=True)
    '''name=db.Column(db.String(150))
    email=db.Column(db.String(150),unique=True)
    contact=db.Column(db.String(100))'''
    heading=db.column(db.String[200])
    sub_heading=db.column(db.String[200])
    category=db.column(db.String[200])
    thimbnail=db.column(db.String[200])
    published_data=db.column(db.DateTime[200])
    description=db.column(db.String[200])
    post_by=db.column(db.String[200])
    status=db.column(db.String[200])

    def user_data(self):
        data={
            'id':self.id,
            # 'name':self.name,
            #'email': self.email,
            # 'contact': self.contact,
            'heading':self.heading,
            'sub_heading':self.sub_heading,
            'category':self.category,
            'thimbnail':self.thimbnail,
            'published_date':self.published_data,
            'description':self.description,
            'post_by':self.post_by,
            'status':self.status


        }
        return data
