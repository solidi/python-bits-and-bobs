from pprint import pprint
from user_schema import UserSchema
from user import User


user_data = {
    'created_at': '2019-05-12T17:26:10.577158+00:00',
    'email': 'monty@python.org',
    'name': 'Monty'
}

#schema = UserSchema()
#result = schema.load(user_data)
#pprint(result)

user_data = {
    'name': 'Ronnie',
    'email': 'ronnie@stones.com'
}

schema = UserSchema()
result = schema.load(user_data)
pprint(result)

user1 = User(name="Mick", email="mick@stones.com")
user2 = User(name="Keith", email="keith@stones.com")
users = [user1, user2]
schema = UserSchema(many=True)
result = schema.dump(users)  # OR UserSchema().dump(users, many=True)
pprint(result)
