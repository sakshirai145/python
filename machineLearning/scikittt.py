import sklearn
from sklearn.datasets import load_iris


from sklearn.datasets import load_iris

iris = load_iris()

from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()

# Print dataset information
print("Feature Names:")
print(iris.feature_names)

print("\nTarget Names:")
print(iris.target_names)

print("\nFirst 5 rows of data:")
print(iris.data[:5])

print("\nFirst 5 target values:")
print(iris.target[:5])

