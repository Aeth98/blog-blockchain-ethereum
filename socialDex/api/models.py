from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from api.utils import sendTransaction
import hashlib

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=32, null=True)
    content = models.TextField()
    hash = models.CharField(max_length=100, default=0, null=True)
    txId = models.CharField(max_length=100, default=0, null=True)

    def writeonChain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = sendTransaction(self.hash)
        self.save()

class UserIp(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)






