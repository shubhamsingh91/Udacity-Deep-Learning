# Scripts for Neural Network perceptron design- Udacity deep learning course

# Importing data from a csv file

import csv
import array as arr
import numpy as nm
import random as rn
import matplotlib.pyplot as plt

# Declaring functions here
# Step function
plt.close('all')

def step_fun(y):
    if (y>=0):
        out = 1
    else:
        out = 0
    return(out)

def pred_fun(w,b,x):
    var3 = nm.dot(w,x_vec)+b
    y_hat = step_fun(var3)
    return(y_hat)

# Preceptron function
def perceptron_fun(w,b,x,lab,alpha):
    train_flag = 0
    y_hat = pred_fun(w,b,x)

    if (y_hat!=lab):
        #print("miss classification here")
        if (y_hat==1): # positive classification but negative label
            #print("positive classification but negative label")
            w[0] = w[0] - alpha*x_vec[0]
            w[1] = w[1] - alpha*x_vec[1]
            b = b - alpha
            train_flag=1
            #print("training here")
        elif (y_hat==0):
            # print("negative classification but positive label")
             w[0] = w[0] + alpha*x_vec[0]
             w[1] = w[1] + alpha*x_vec[1]
             b = b + alpha
             train_flag=1
             #print("training here")
    return w,b, train_flag


# Importing data

with open('/Users/singh281/Desktop/Scripts/Python test/Udacity DL/data1.csv','r') as file:
    var_row = csv.reader(file)
    cont=0
    x1 = []
    x2 = []
    lab = []
    for row in var_row:
        x1.append(float(row[0])) # x1 column
        x2.append(float(row[1])) # x2 column
        lab.append(int(row[2])) # label column

data_size = len(x1)
n = 2 # variable data_size

# Formulating the model and prediction- y_hat

# randomizing w and b variables

w = []
for ii in range(1,3):
    var2 = rn.random()
    w.append(var2)
    #print(ii)

b = rn.random()

# Calculating the prediction here for all data- just once, or the perceptron step

x_vec = [0,0]
alpha = 0.1 # learning rate

# plotting points here
for ii in range(data_size):
    x_vec[0] = x1[ii]
    x_vec[1] = x2[ii]
    plt.scatter(x_vec[0],x_vec[1])
    plt.show()


# for ii in range(data_size):
#     x_vec[0] = x1[ii]
#     x_vec[1] = x2[ii]
#     lab_in = lab[ii]
#     w,b, train_flag = perceptron_fun(w,b,x_vec,lab_in,alpha)
#     print(train_flag)
#
# print(w,b)
