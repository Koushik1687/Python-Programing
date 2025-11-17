# WAP: Simulated Annealing
import matplotlib.pyplot as plt

num = 100
tem = 10

iterations = [i for i in range(num)]
tem2 = [tem / float(i + 1) for i in iterations]

plt.plot(iterations, tem2, marker='o', linestyle='-',)
plt.xlabel('Iteration')
plt.ylabel('Temperature')
plt.title("Temperature Decay (Simulated Annealing)")
plt.show()
