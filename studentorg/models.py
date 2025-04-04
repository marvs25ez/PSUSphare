from django.db import models

# Create your models here.
class BaseModel(models.Model) :
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at =models.DateTimeField(auto_now_add=True)

    class Meta :
        abstract = True

class college(BaseModel):
    college_name = models.CharField(max_length=150)
'''
    def__str__(self):
        return self.college_name
'''
class program(BaseModel):
    prog_name =  models.CharField(max_length=150)
    college =  models.ForeignKey(College, on_delete=models.CASCADE)



