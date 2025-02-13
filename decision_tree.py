#-------------------------------------------------------------------------
# AUTHOR: Jairus Legion
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4210- Assignment #1
# TIME SPENT: 5 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

featureMap = {}
#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
#--> add your Python code here
# X =
for col in range(len(db[0]) - 1):
    values = set()
    for row in db:
        values.add(row[col])
    sortedVals = sorted(values)
    temp = {}
    for i, val in enumerate(sortedVals):
        temp[val] = i
    featureMap[col] = temp

#print(featureMap)
for row in db:
    featureNums = []
    for col in range(len(db[0]) - 1):
        featureNums.append(featureMap[col][row[col]])

    X.append(featureNums)

#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2
#--> addd your Python code here
# Y =
for row in db:
    if row[-1] == "Yes":
        Y.append(1)
    else:
        Y.append(2)


#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()