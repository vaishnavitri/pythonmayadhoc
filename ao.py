#!usr/bin/python3

#features differenciating  = texture,weight

from sklearn import tree
 

features=[[120,0],[110,0],[130,1],[140,1]]
output=["apples","apples","orange","orange"]

#loading decision tree classifier
algo=tree.DecisionTreeClassifier()

#trianing the prog
train=algo.fit(features,output)     #requires 1 core CPU[/GPU]

#QNA

out=train.predict([[120,1]])


print (out)
