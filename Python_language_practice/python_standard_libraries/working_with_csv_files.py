import csv
# writing data to file
"""with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", "product_id", "price"])
    writer.writerow([1000, 1, 100])
    writer.writerow([1001, 2, 200])
    writer.writerow([1002, 3, 300])"""

# reading data from file
with open("data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    # by iterating reader second time we are at the end of file so no output is printed
    for read in reader:
        print(read)
