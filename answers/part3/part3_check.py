import numpy as np
import pandas as pd
import torch

def loss1_check(loss1):

    print(loss1)
    if loss1 > 2.5 or loss1 < 2.0 :
        print("'loss1' is not on correct level. Please check your answer.")

    else :
        print("'loss1' is ok!")
    

def training_loss2_check(training_loss2):

    print(training_loss2)
    if len(training_loss2) != 5 :
        print("'training_loss2' lenght is not correct. Please check your answer.")
    
    elif training_loss2[0] > 2.1 or training_loss2[0] < 1.8 :
        print("'training_loss2' first element is not on correct level. Please check your answer.")

    elif training_loss2[4] > 0.5 or training_loss2[4] < 0.2 :
        print("'training_loss2' last element is not on correct level. Please check your answer.")

    else :
        print("'training_loss2' is ok!")
    

