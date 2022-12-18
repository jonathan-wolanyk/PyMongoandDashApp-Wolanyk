from pymongo import MongoClient
from bson.objectid import ObjectId
from urllib.parse import urlparse

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:39244/AAC' % (username, password))
        self.database = self.client['AAC']
        
        
    # Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            return self.database.animals.insert(data)  # data should be dictionary 
        else:
            raise Exception("Nothing to save, because data parameter is empty")


    # Create method to implement the R in CRUD. 
    def read(self, data):
        if data is not None:
            return self.database.animals.find(data, {"_id": False})
        else:
            raise Exception("Nothing to save, because data parameter is empty")
        
    # Create method to implement the U in CRUD.
    def update(self, searchTerm, data):
        if data is not None:    
            data_update = self.database.animals.update_one(searchTerm, data)
            return data_update
        else:
            raise Exception("Nothing to update because data parameter is empty")
          
    # Create method to implement the D in CRUD.
    def delete(self,data):
        if data is not None:    
            return self.database.animals.delete_one(data)
        else:
            raise Exception("Nothing to delete because data parameter is empty")