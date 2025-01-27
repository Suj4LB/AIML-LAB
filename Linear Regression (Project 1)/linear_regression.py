import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#Took data from caggle

df = pd.read_csv("data.csv")
print(df)


x = np.array(df["Height(Inches)"])
y = np.array(df["Weight(Pounds)"])
m = len(x)

alpha = 0.0001
cost_threshold = 0.001
max_iterations = 1000

theta_0 = 0
theta_1 = 0


plt.scatter(x, y, label="Data points")
plt.plot(x, theta_0 + x * theta_1, color="red", label="Regression line")
plt.legend()
plt.show()


def hypothesis(x):
    return theta_0 + x * theta_1

def cost():
    # square_cost = 0
    # for i in range(m):
    #     square_cost += (hypothesis(x[i]) - y[i]) ** 2

    # return (1/(2*m)) * square_cost

    diff = hypothesis(x) - y
    return (1 / (2 * m)) * np.sum(diff ** 2)

def pd_theta_0():
    # sum_term = 0
    # for i in range(m):
    #     sum_term += hypothesis(x[i]) - y[i]

    # return (1/m) * sum_term

    diff = hypothesis(x) - y
    return (1 / m) * np.sum(diff)

def pd_theta_1():
    # sum_term = 0
    # for i in range(m):
    #     sum_term += (hypothesis(x[i]) - y[i]) * x[i]

    # return (1/m) * sum_term

    diff = hypothesis(x) - y
    return (1 / m) * np.sum(diff * x)


iteration = 0

theta_0_graph = dict()
theta_1_graph = dict()

while cost() > cost_threshold and iteration < max_iterations:
    cost_val = cost()

    theta_0_graph[cost_val] = theta_0
    theta_1_graph[cost_val] = theta_1

    theta_0 -= alpha * pd_theta_0()
    theta_1 -= alpha * pd_theta_1()
    iteration += 1

    if iteration % 100 == 0:
        print(f"Iteration {iteration}: Cost = {cost()}")

print(f"Theta 0 : {theta_0}\nTheta 1 : {theta_1}")


plt.scatter(x, y, label="Data points")
plt.plot(x, theta_0 + x * theta_1, color="red", label="Regression line")
plt.legend()
plt.show()