from django.db import models

class Todo(models.Model):
    task_name = models.CharField(max_length=120,null=True)
    choices=(("completed","completed"),
             ("notcompleted","notcompleted"))
    status = models.CharField(max_length=12,choices=choices,default="notcompleted")
    user=models.CharField(max_length=120)

    def __str__(self):
        return self.user
