from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow 


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/persons'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

class Person(db.Model):
    __tablename__ = 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    email = db.Column(db.String(80), unique=True)
    designation = db.Column(db.String(80))
    age = db.Column(db.Integer)

    def __init__(self, name, email, designation, age):
        self.name = name
        self.email = email
        self.designation = designation 
        self.age = age 

    def __repr__(self):
        return {'name': self.name, 'email': self.email, 'designation': self.designation, 'age': self.age}

    def __str__(self):
        return 'Person(name='+self.name+', email='+self.email+', designation='+self.designation+', age='+str(self.age)+')'


class PersonSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'designation', 'age')

person_schema = PersonSchema()
persons_schema = PersonSchema(many=True)


@app.route('/')
def index():
    return 'Hello World!'

@app.route('/api/v1/insert', methods=['POST', 'GET'])
def insert():

    if request.method == 'POST':
        name = request.json['name']
        email = request.json['email']
        age = request.json['age']
        designation = request.json['designation']

        new_person = Person(name, email, designation, age)
        db.session.add(new_person)
        db.session.commit()
        
        return "New Entry Added in the database"
    else:
        return "No Data!"

@app.route('/api/v1/getall', methods=['GET'])
def getall():
    all_persons = Person.query.all()
    result = persons_schema.dump(all_persons)
    return jsonify(result)


@app.route('/api/v1/get/<name>', methods=['GET'])
def getone(name):
    find_person = Person.query.filter_by(name=name).first()
    return person_schema.jsonify(find_person)

@app.route('/api/v1/update/<name>', methods=['PUT', 'GET'])
def update(name):

    if request.method == 'PUT':
        find_person = Person.query.filter_by(name=name).first()

        name = request.json['name']
        email = request.json['email']
        age = request.json['age']
        designation = request.json['designation']

        find_person.name = name
        find_person.age = age 
        find_person.email = email 
        find_person.designation = designation

        db.session.commit()

        return person_schema.jsonify(find_person)

    else:
        return "No Modification!"

@app.route('/api/v1/delete/<name>', methods=['GET', 'DELETE'])
def delete(name):
    if request.method == 'DELETE':
        find_person = Person.query.filter_by(name=name).first()
        db.session.delete(find_person)
        db.session.commit()

        return person_schema.jsonify(find_person)

if __name__ == "__main__":
    manager.run()
    # app.run(debug=True)