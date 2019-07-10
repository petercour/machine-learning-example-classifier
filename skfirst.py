
import sklearn;
from sklearn import tree
from sklearn.naive_bayes import GaussianNB
from sklearn import neighbors

# training data
X = [[0,90], [0,80], [1,20], [1,60], [0,70],[0,70],[1,99]]
Y = ['heisenberg','heisenberg','garbage','garbage','garbage', 'garbage', 'garbage']

# new data for prediction
color = input("Enter color: ")
if color == "blue":
    color = 0.0
else:
    color = 1.0

pure = input("How many percent pure: ")
pure = float(pure)

P = [[color,pure]]

# make prediction
c = tree.DecisionTreeClassifier()
c = c.fit(X,Y)
print("\nPrediction : " + str(c.predict(P)))
