def build_car(manufacturer,model,**car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key,value in car_info.items():
        car[key] = value
    return car

new_car = build_car('honda','civic',color='blue',mileage='60,000 miles')
print(new_car)