from django.db import models
from django.utils import timezone

# Create your models here.

class Felix_class(models.Model):
          FELIX_CLASS_TYPES=[
              ('FSP','FULL STACK PYTHON'),
              ('FSJ','FULL STACK JAVA')  , 
              ('DS','DATA SCIENCE') ,
              ('ML','MACHINE LEARNING'),
              ('UI/UX','UI/UX'),
              ('DA','DATA ANALYST')
          ]
          name =models.CharField(max_length=100)
          img = models.ImageField(upload_to='images/')
          date = models.DateTimeField(default=timezone.now)
          type = models.CharField(max_length=100,choices=FELIX_CLASS_TYPES)
          duration = models.CharField(max_length=100)


          def __str__(self):
                  return self.name