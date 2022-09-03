from datetime import datetime
import uuid
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)
            

    def __str__(self):
        return '[{}] ({}) {}'.format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        my_dict = self.__dict__.copy()
        # adding a key __Class__ and assign it a class name of the created object
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
