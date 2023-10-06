from services.user_service import UserService

def create_user(data):
    user, error_message = UserService.create_user(data)
    return user, error_message