from marshmallow import pprint
from user import User
from user_schema import UserSchema

user = User(name="Monty", email="monty@python.org")
schema = UserSchema()
result = schema.dump(user)
pprint(result)

json_result = schema.dumps(user)
pprint(json_result)

summary_schema = UserSchema(only=('name', 'email'))
print(summary_schema.dump(user))