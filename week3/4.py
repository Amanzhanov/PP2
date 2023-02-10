def my_function(**product_properties):
  print("product name" + product_properties["name"])
  print("product price" + product_properties["price"])
  print("product duration" + product_properties["duration"])
  for k in product_properties:
    print(k)

my_function(name = "Deposit" , price = "12.5%" , duration = "12 m.")