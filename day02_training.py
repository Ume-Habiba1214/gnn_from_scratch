xs = [1, 2, 3, 4] # inputs
ys = [2, 4, 6, 8] # correct answers


def predict(weight, x):     
    """Return the guess for a given weight and input."""
    return weight * x

def loss_one(weight, x, y):
    """Return the squared error loss for a given weight, input, and correct answer."""
    guess = predict(weight, x)
    return (guess - y) ** 2

def loss(weight, xs, ys):
    """Return the average loss for a given weight and a list of inputs and correct answers."""
    total_loss = 0
    for x, y in zip(xs, ys):
        total_loss += loss_one(weight, x, y)
    return total_loss / len(xs)

def gradient_one(weight, x, y):
    """Return the gradient of the loss with respect to the weight."""
    guess = predict(weight, x)
    return 2 * x * (guess - y)

def gradient(weight, xs, ys):
    """Return the average gradient of the loss with respect to the weight for a list of inputs and correct answers."""
    total_gradient = 0
    for x, y in zip(xs, ys):
        total_gradient += gradient_one(weight, x, y)
    return total_gradient / len(xs)


weight = 0.0  # initial weight
learning_rate = 0.01
for epoch in range(1, 50):
    grad = gradient(weight, xs, ys)
    weight -= learning_rate * grad
    current_loss = loss(weight, xs, ys)
    print(f"Epoch {epoch}: weight = {weight:.4f}, loss = {current_loss:.4f}")