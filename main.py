inputs = [3, 5, 2]

weights = [0.4, 0.8, 0.2]

bias = 2

output = []
for x, y in zip(inputs, weights):
   output.append(x*y+bias)

print(output)
# In way over my head with this right now, ill return when im not brain damaged...
