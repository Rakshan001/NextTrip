# from django.db import models
# from django.contrib.auth.models import User


# class Station(models.Model):
#     name = models.CharField(max_length=100)

# class Bus(models.Model):
#     number = models.CharField(max_length=20)
#     name = models.CharField(max_length=100)
#     reg_number = models.CharField(max_length=20)
#     capacity = models.IntegerField()
#     image = models.ImageField(upload_to='bus_images')  # Store image

# class Route(models.Model):
#     start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_routes')
#     end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_routes')
#     distance = models.FloatField()
#     cost = models.FloatField()
#     bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

# class Trip(models.Model):
#     route = models.ForeignKey(Route, on_delete=models.CASCADE)
#     departure_time = models.DateTimeField()
#     available_seats = models.IntegerField(default=0)









# ***********************************************
# from django.db import models

# class Station(models.Model):
#     name = models.CharField(max_length=100)

# class Bus(models.Model):
#     number = models.CharField(max_length=20)
#     name = models.CharField(max_length=100)
#     reg_number = models.CharField(max_length=20)
#     capacity = models.IntegerField()
#     image = models.ImageField(upload_to='bus_images')  # Store image

#     def __str__(self):
#         return self.name

# class Route(models.Model):
#     start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_routes')
#     end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_routes')
#     distance = models.FloatField()
#     cost = models.FloatField()
#     bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.start_station} to {self.end_station}"


# class Stop(models.Model):
#     route = models.ForeignKey(Route, on_delete=models.CASCADE)
#     station = models.ForeignKey(Station, on_delete=models.CASCADE)
#     order = models.IntegerField()  # To specify the stop's position in the route
#     def __str__(self):
#         return self.station


# class Trip(models.Model):
#     route = models.ForeignKey(Route, on_delete=models.CASCADE)
#     departure_time = models.DateTimeField()
#     available_seats = models.IntegerField(default=0)
#     def __str__(self):
#         return self.route



#################################
from django.db import models

class Station(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Bus(models.Model):
    number = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    capacity = models.IntegerField()
    # image = models.ImageField(upload_to='bus_images')  # Store image

    def __str__(self):
        return self.name

class Route(models.Model):
    start_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='start_routes')
    end_station = models.ForeignKey(Station, on_delete=models.CASCADE, related_name='end_routes')
    distance = models.FloatField()
    cost = models.FloatField()
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.start_station} to {self.end_station} =>{self.bus.name} "

class Stop(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    order = models.IntegerField()  # To specify the stop's position in the route
    arrival_time=models.TimeField()

    def __str__(self):
        # return str(self.station)
        return f"{self.station} - {self.arrival_time} Route:=> - {self.route}"

class Trip(models.Model):
    route = models.ForeignKey(Route, on_delete=models.CASCADE)
    departure_date= models.DateField()
    departure_time = models.TimeField()
    available_seats = models.IntegerField(default=0)

    # def __str__(self):
    #     return str(self.route)
    def __str__(self):
        return f"{self.route} :=> (Bus: {self.route.bus.number}-{self.route.bus.name}) {self.departure_date} =>{self.departure_time}"

