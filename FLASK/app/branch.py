
from app.orm import ORM

class Branch(ORM):

    tablename = 'branch'
    fields = ['pk', 'name', 'city']

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.get('pk')
        self.name = kwargs.get('name')
        self.city = kwargs.get('city')

    
