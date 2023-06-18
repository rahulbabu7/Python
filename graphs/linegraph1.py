import matplotlib.pyplot as plt

years= [1903, 1912, 1915, 1916, 1918, 2004, 2007, 2013]
homeRuns = [48,29,14,14,15,222,166,178]

plt.title("Example",color="blue",size = 15) #!gives title to the graph
plt.xlabel("YEARS")
plt.ylabel("Runs")
plt.plot(years,homeRuns,'g-o',) #!g-o gives circle dot on graph o is the shape
plt.show()