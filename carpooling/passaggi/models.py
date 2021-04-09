from django.db import models
import uuid
# Create your models here.
class Type_Vehicle(models.Model):
    """Model representing a type vehicle."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    description = models.CharField(max_length=45, help_text='Enter a type vehicle')

    def __str__(self):
        """String for representing the Model object."""
        return self.description
class User(models.Model):
    """Model representing an user."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    email = models.CharField(max_length=45, help_text='Enter an email')
    encrypted_password=models.CharField(max_length=45)
    admin=models.BooleanField()
    active=models.BooleanField()

    def __str__(self):
        """String for representing the Model object."""
        return self.email
class Profile( models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50, help_text='Enter the name')
    surname = models.CharField(max_length=50, help_text='Enter the surname')
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    mobile = models.CharField(max_length=20)
    description=models.TextField(max_length=1000)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.name},{self.surname}'
class Vehicle( models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    brand = models.CharField(max_length=45, help_text='Enter the brand')
    model = models.CharField(max_length=45, help_text='Enter the model')
    colour = models.CharField(max_length=45)
    motor = models.CharField(max_length=20)
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    type_vehicle_id = models.ForeignKey('Type_vehicle', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.brand},{self.model}'
class Preference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    conversation=models.BooleanField()
    animal=models.BooleanField()
    smoke=models.BooleanField()
    music=models.BooleanField()
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.animal},{self.smoke},{self.conversation},{self.music}'
class Scores(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    scores=models.IntegerField()
    count=models.IntegerField()
    total=models.IntegerField()
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.scores},{self.count},{self.total}'
class Path_Offer( models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    departure = models.CharField(max_length=100, help_text='Enter the departure')
    arrive = models.CharField(max_length=100, help_text='Enter the arrive')
    data_partenza=models.DateField(help_text="Enter la data di partenza")
    data_arrivo=models.DateField(help_text="Enter la data di arrivo")
    ora_partenza = models.DateTimeField(help_text="Enter l'ora di partenza")
    ora_arrivo = models.DateTimeField(help_text="Enter l'ora di arrivo")
    user_id = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    vehicle_id = models.ForeignKey('Vehicle', on_delete=models.SET_NULL, null=True)
    max_avalaible=models.IntegerField()
    price=models.FloatField()
    full=models.BooleanField()
    booked=models.BooleanField()

    def __str__(self):
        return f'{self.departure},{self.arrive},{self.data_partenza},{self.data_arrivo},{self.ora_partenza},{self.ora_arrivo}'
class Feedback(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    scores=models.IntegerField()
    feedback=models.TextField()
    title=models.CharField(max_length=45)
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    path_offer_id=models.ForeignKey('Path_Offer', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.feedback},{self.title},{self.scores}'
class Feedback_Path(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    booked=models.IntegerField()
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    path_offer_id=models.ForeignKey('Path_Offer', on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'{self.user_id},{self.path_offer_id},{self.booked}'
class Message(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user_id=models.ForeignKey('User', on_delete=models.SET_NULL, null=True)
    dest_user_id = models.CharField(max_length=45)
    path_offer_id=models.ForeignKey('Path_Offer', on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=45)
    message=models.CharField(max_length=45)
    read=models.BooleanField()
    def __str__(self):
        return f'{self.user_id},{self.dest_user_id},{self.title},{self.message}'




