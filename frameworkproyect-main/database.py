from peewee import *

database = MySQLDatabase(
    'proyectflp',
    user='root', password='',
    host='localhost', port=3306
)
class User(Model):
    username= CharField(max_length=50, unique=True)
    email= CharField(max_length=50)
    password= CharField(max_length=32)
    
    def __str__(self):
        return self.username
    
    class Meta:
        database = database
        table_name = 'users'
#class cancion
#class post
#class perfil