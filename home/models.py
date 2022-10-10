from django.db import models

class Contact(models.Model):
      name = models.CharField(max_length=15)
      email= models.EmailField()
      message = models.TextField()

      SUBJECT = [
            ('MF' , 'Üretim'),
            ('SH', 'Nakliye'),
            ('AD', 'Yönetim'),
            ('HR', 'İnsan Kaynakları')
      ]

      sub = models.CharField(max_length=2, choices=SUBJECT, default=SUBJECT[3][0])

