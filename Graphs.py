import matplotlib.pyplot as plt

# very basic plot
# x = [1, 3, 5, 10]  # data to plot
# plt.plot(x)
# plt.show()  # shows plot

# plotting x and y against each other
# y = [7, 12, 21, 22]
# plt.plot(x, y)
# plt.show()

# plot a nicer plot - line 1
x = [3, 9, 14,]
y = [2, 7, 30]
plt.plot(x, y, c="green", linewidth=2, label="Line 1")

# plotting 2 lines on the same graph - line 2
x2 = [1, 15, 18]
y2 = [0, 3, 12]
plt.plot(x2, y2, c="red", linewidth=2, label="Line 2", linestyle="dashed",
         marker="o", markerfacecolor="orange", markersize=10)

# labelling axis and title, plus legend
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Two Lines")

# limit of axis
plt.ylim(1, 10)
plt.xlim(0, 30)

plt.legend()
plt.show()
