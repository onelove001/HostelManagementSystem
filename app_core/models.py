from django.db import models
from django.contrib.auth.models import User



class Student_Account(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    matric = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    is_student = models.BooleanField(default = True)
    wallet = models.IntegerField(default = 0, null = True)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username


class Deposit(models.Model):
    student = models.ForeignKey(Student_Account, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 200)
    card_number = models.CharField(max_length=20)
    cvv = models.CharField(max_length = 6)
    expire = models.CharField(max_length = 6)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.student.user.username


class House_Manager(models.Model):
    full_name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    phone_no = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.full_name


class Block(models.Model):
    house_manager = models.ForeignKey(House_Manager, on_delete = models.CASCADE)
    block_name = models.CharField(max_length = 50)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.block_name


class Rooms(models.Model):
    block = models.ForeignKey(Block, on_delete = models.CASCADE)
    room_name = models.CharField(max_length = 50, null=True)
    room_tag = models.CharField(max_length = 10, default="NEW")
    description = models.TextField()
    condition = models.TextField()
    charge = models.IntegerField()
    is_available = models.BooleanField(default=True)
    image1 = models.FileField(default="default.png")
    image2 = models.FileField(default="default.png")
    image3 = models.FileField(default="default.png")
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.room_name


class Accomodation_Request(models.Model):
    student = models.OneToOneField(Student_Account, on_delete = models.CASCADE)
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)


    def __str__(self):
        return f"{self.room.room_name} has been {self.approved} {self.student.first_name}"



class Complaints(models.Model):
    student = models.ForeignKey(Student_Account, on_delete = models.CASCADE)
    subject = models.CharField(max_length = 40)
    message = models.TextField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.student.first_name} - {self.subject}"



class GuestStayRequest(models.Model):
    student = models.ForeignKey(Student_Account, on_delete = models.CASCADE)
    full_name = models.CharField(max_length = 40)
    address = models.CharField(max_length = 40)
    reason = models.TextField()
    status = models.BooleanField(default=False)
    date_from = models.DateField()
    date_to = models.DateField()
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.student.first_name} - {self.full_name}"


class RoomTransfer(models.Model):
    student = models.ForeignKey(Student_Account, on_delete=models.CASCADE)
    reason = models.TextField()
    room = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.student.first_name} - {self.room.room_name}"



class Guideline(models.Model):
    rule = models.TextField()
    guideline1 = models.CharField(max_length = 250)
    guideline2 = models.CharField(max_length = 250)
    guideline3 = models.CharField(max_length = 250)
    guideline4 = models.CharField(max_length = 250)
    guideline5 = models.CharField(max_length = 250)
    created_at = models.DateTimeField(auto_now = True)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.rule[:20]}"
