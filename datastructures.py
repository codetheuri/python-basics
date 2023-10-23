# list
fruits=["oranges","bananas","maongoes","apples"]
numbers=[1,3,7,5,4]
numbers.sort()
numbers[4]=9
rep=numbers*2
print(fruits)
print(f"i love eating {fruits[2]}")
print(numbers)
print(rep)

# tuples
cars=("toyota","nissan","benz","isuzu","nissan")
places=(2,3,4,5,["msa","nrb","klf"])
print(places)
print(cars)
print(cars[2])
repeat=cars*2
print(repeat)
print(repeat.count("nissan"))

# sets unorded
days={"sunday","monday","tuesday"}
print(days)

# dictionary

staff_details= {"name:" :"Joseph","age" :19,"sector": "backend"}
print(staff_details)
print("your name is  %s" %staff_details["name:"])
print("your age is %d" %staff_details["age"])
print("your sector is %s" %staff_details["sector"])