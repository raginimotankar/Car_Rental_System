from car import Car
from customer import Customer
from rental import Rental
#create cars
car1=Car("C001","Toyata","Innova",2022)
car2=Car("C002","Honda","Accord",2022)
#create customer
customer1=Customer("CU001","Nishid Jojare")
customer2=Customer("CU002","Vivek nimbholkar")
#rent cars
customer1.rent_car(car1)
customer2.rent_car(car2)
#display rented cars for customers
print(f"{customer1.name}'s Rented Cars:{[car.make for car in customer1.rented_cars]}")
print(f"{customer2.name}'s Rented Cars:{[car.make for car in customer2.rented_cars]}")
#return cars
customer1.return_car(car1)
#display updated rented cars for customer
print(f"{customer1.name}'s Updated Rented Cars:{[car.make for car in customer1.rented_cars]}")
print(f"{customer2.name}'s Updated Rented Cars:{[car.make for car in customer2.rented_cars]}")
#create rentals
rental1=Rental("R001",customer1,car1,rental_fee=500.0)
rental2=Rental("R002",customer2,car2,rental_fee=450.0)
#display rental information
print(f"Rental ID:{rental2.rental_id},Customer:{rental2.customer.name},Car:{rental2.car.make},Rental Fee:INR{rental2.rental_fee}")
