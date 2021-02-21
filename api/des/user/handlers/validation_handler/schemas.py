email_schema = {
    'type': 'string',
    'regex': '^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$',
    'required': True
}
username_schema = {
    'type': 'string',
    'regex': '^[A-z0-9_-]{3,20}$',
    'required': True
}
password_schema = {
    'type': 'string',
    'regex': '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9]).{8,}$',
    'required': True,
}
registration_schema = {
    'email': email_schema,
    'username': username_schema,
    'password': password_schema
}

login_schema = {
    'email': email_schema,
    'password': password_schema
}
