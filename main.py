#zadanie1
shopping_list={
    "piekarnia": ["bagietka", "kajzerka", "grahamka","chałka"],
    "warzywiak": ["marchewka", "cebula","sałata"],
    "mięsny": ["schab", "szynka"]
}
number_of_products=[]
for shop, products in shopping_list.items():
    for n in products:
        Products=[]
        for n in products:
            Products.append(n.capitalize())
    print(f"Idę do {shop.capitalize()} i kupuję tam: {Products}")
    number_of_products.append(len(products))
print("W sumie kupuję " + str(sum(number_of_products))+" produktów")

#zadanie 2
list_100=[]
for i in range (0,101):
    list_100.append(i)
print(list_100)

list_divided_by_5=[]
for n in list_100:
    if n%5==0:
      list_divided_by_5.append(n)
print(list_divided_by_5)

list_cube_numbers=[]
list_cube_numbers = [n**3 for n in list_100]
print(list_cube_numbers)