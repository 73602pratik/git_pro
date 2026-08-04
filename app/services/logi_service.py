def authenticate_student(username, password):
    if username == "admin" and password == "password":
        return "Login Successful"
    return "Invalid Credentials"