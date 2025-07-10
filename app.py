from flask import Flask,jsonify,request
from config import SQLALCHEMY_DATABASE_URI, SQL_ALCHEMY_TRACK_MODIFICATIONS
from models.users import db, Users

app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATION']= SQL_ALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)

@app.route('/listuser')
def list_user():
    users=Users.query.all()
    return jsonify([data.user_data] for data in users)

@app.route('/user_details/<int;id>',methods=['GET'])
def user_details(id):
    user=Users.query.get_or_404(id)
    return jsonify(user.user_data())

@app.route('/save_user',methods=['POST'])
def save():
    data=request.json
    user=Users(id=data['id'], heading=data['heading'], sub_heading=data['sub_heading'], category=data['category'], thimbnail=data['thimbnail'], published=data['published'], description=data['description'], post_by=data['post_by'], status=data['status'])
    db.session.add(user)
    db.session.commit()
    return jsonify(user.user_data()),201
    
if __name__ == '__main__':
    app.run(debug=True)