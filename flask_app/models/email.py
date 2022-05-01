import email
import imp, re
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db ="emails_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @staticmethod
    def validate_form(form_data):
        is_valid = True
        if not EMAIL_REGEX.match(form_data['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid
    @classmethod
    def get_one(cls, id):
        query  = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, {'id':id})
        print(result)
        return cls(result[0])
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (email) VALUES (%(email)s);"
        return connectToMySQL(db).query_db( query, data )  
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(db).query_db(query)
        emails = []
        for email in results:
            emails.append( cls(email) )
        return emails
