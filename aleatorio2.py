favourite_three_franchises = [
  {
    "Name" : "Call of Duty", 
    "Units Sold" : 400
  },
  {
    "Name" : "Final Fantasy",
    "Units Sold" : 150
  },
  {
    "Name" : "Mass Effect",
    "Units Sold" : 16
  }
]

for i in range(len(favourite_three_franchises)):
    if favourite_three_franchises[i]["Name"] == 'Call of Duty':
        print(f'Units Sold: {favourite_three_franchises[i]["Units Sold"]} million')