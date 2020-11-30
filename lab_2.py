import matplotlib.pyplot as plt

picture = plt.figure(figsize=(9.6, 5.4))

ds = input("Введіть назву файлу с датасетом. Приклад: Data1.txt\n")

with open(ds, 'r') as data:
    lines = data.readlines()
    x = [float(line.split()[0]) for line in lines]
    y = [float(line.split()[1]) for line in lines]

plt.scatter(y,x,color = "black")
picture.savefig('data_picture_2.jpg')

plt.show()
