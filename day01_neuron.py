"""
A neuron:
  1. multiplies each feature by its own weight
  2. adds everything up, plus a bias
  3. passes the result through an activation function (ReLU)

Building it without any libraries, just Python.
"""



def relu(x):
    """ReLU: negative numbers become 0, positive numbers stay the same. 
    This is activation function.(rectified linear unit )"""
    if x < 0:
        return 0
    return x



def neuron(features, weights, bias):
    """One neuron: weighted sum of the features, plus bias, then ReLU. 
    zip takes two (or more) lists and pairs up their items by position:
    first with first, second with second, and so on."""
    total = bias
    for feature, weight in zip(features, weights):
        total = total + feature * weight
    return relu(total)



# Test the ReLU function with a negative and a positive number
print("ReLU(-3) =", relu(-3))   # expected 0
print("ReLU(4)  =", relu(4))    # expected 4
print()



# house with 2 features: [size, rooms] and a bias
# features = [size in m2, number of rooms]
house = [100, 3]
weights = [3000, 10000]
bias = 20000
price = neuron(house, weights, bias)
print("House with features: ", house, "-> guessed price:", price, "EUR")   # expected 350000
print()




#house with 3 features: [size, rooms, has_toilet (1 or 0)] and a bias
my_house = [100, 3, 1]
my_weights = [3000, 10000, 5000]
my_bias = 20000
print("My house", my_house, "-> guessed price:",
      neuron(my_house, my_weights, my_bias), "EUR")       # expected 355000
print()




# Each neuron has its own weights, so each one "notices" something different.
# The layer turns a vector of 2 numbers into a new vector of 3 numbers.
layer_weights = [
    [1, 2],     # neuron 1
    [-1, 1],    # neuron 2
    [0.5, -4],  # neuron 3
]
layer_biases = [0, 0, 1]
x = [2, 3]
new_vector = [neuron(x, w, b) for w, b in zip(layer_weights, layer_biases)]
print("Layer input :", x)
print("Layer output:", new_vector)   # expected [8, 1, 0]


#adding layer 2
layer2_weights = [
    [1, 1, 1],  # neuron A
    [2, -1, 3],  # neuron B
    [8, -1, 0],  # neuron C
    [5, -7, 3],  # neuron D
    [2, 1, 3],  # neuron E
]
layer2_biases = [0, -5, 2, 3, 1]
layer2_vector=[neuron(new_vector, w, b) for w, b in zip(layer2_weights, layer2_biases)]
print("Layer 2 input :", new_vector)
print("Layer 2 output:", layer2_vector)   # expected [9, 10, 65, 36, 18]