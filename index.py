from appliances import DishWasher, Washer, Dryer, Refrigerator, CoffeeMaker, Stove, CanOpener

whirlpool_dishwasher = DishWasher("black")
whirlpool_dishwasher.wash_dishes()
print(whirlpool_dishwasher)

samsung_washer = Washer("red", "heater")
samsung_washer.wash_clothes("del")
print(samsung_washer)

samsung_dryer = Dryer("red", "gas")
samsung_dryer.dry_clothes("med")
print(samsung_dryer)

lg_fridge = Refrigerator("stainless")
lg_fridge.make_ice()
print(lg_fridge)

mr_coffee = CoffeeMaker("white")
mr_coffee.make_coffee()
print(mr_coffee)

stove_brand = Stove("white")
stove_brand.cook_food()
print(stove_brand)

starbucks = CoffeeMaker("white")
starbucks.make_coffee()
print(starbucks)

canopen = CanOpener("white")
canopen.open_can()
print(canopen)
