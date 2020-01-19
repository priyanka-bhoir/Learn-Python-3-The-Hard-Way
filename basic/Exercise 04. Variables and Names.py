car=100
Space_in_car=4 #underscope character
driver=30
passa=90
car_driven=driver
cars_not_driven=car - driver
carpool_capacity=car_driven*Space_in_car
avg_passen=passa/car_driven

print("There are",car,"cars available")
print("There are only",driver,"drivers available")
print("There will be",cars_not_driven,"empty cars today")
print("We can transport",carpool_capacity,"people today")
print("We have",passa,"to carry today")
print("We need to put about",avg_passen,"in each car")
