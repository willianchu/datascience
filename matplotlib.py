import matplotlib.pyplot as plt

plt.figure() #The Frame: We start our plot with a figure
plt.bar(x = data, height = data) #The Body: Declaring the specific bar plot
plt.title("Example Bar Plot") #Stylistic Features: Adding the title
plt.show() #To show our plot, we need to end our plot with a plt.show()

data = {'item_1':40, 'item_2':50, 'item_3':25} 
items = list(data.keys())
quantity = list(data.values())


plt.figure()
plt.bar(x = items, height = quantity)
plt.show()
