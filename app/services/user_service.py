# services/user_service.py
from flask import jsonify
from app.models import User  # Import your User model


class UserService:
    @staticmethod
    def create_user(payload):
        try:
            # Check if the user already exists
            print("1 coming till here")
            username, email, password, first_name, last_name,  pan_number = payload
            print("coming till here")
            
            if not username or not email or not pan_number:
                return None, "Username, email, or PAN number is missing"

            existing_user = User.query.filter_by(username=username).first()
            if existing_user:
                return None, "Username already exists"
            
            # Create a new user
            new_user = User(
                username=username,
                email=email,
                password=password,  # Hash the password before storing it (not shown in this example)
                first_name=first_name,
                last_name=last_name,
                pan_number=pan_number
            )
            response = new_user.create()  # Assuming User model has a `save` method for adding to the database
            return "user created successfully", None
        except Exception as e:
            print(e)
            return None, str(e)
        
    @staticmethod
    def get_user_by_username(username):
        return User.query.filter_by(username=username).first()

    @staticmethod
    def update_user(user, new_data):
        try:
            for key, value in new_data.items():
                setattr(user, key, value)
            user.save()  # Assuming User model has a `save` method for updating in the database
            return user, None
        except Exception as e:
            return None, str(e)
