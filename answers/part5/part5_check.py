import numpy as np
import pandas as pd
import torch

def losses_check(train_losses1, test_losses1, train_losses2, test_losses2):

    print("Without dropout")
    print("Train loss: ", train_losses1[-1])
    print("Test loss: ", test_losses1[-1])
    print("\nWith dropout")
    print("Train loss: ", train_losses2[-1])
    print("Test loss: ", test_losses2[-1])
    
    if train_losses1[-1] > 0.5 or train_losses1[-1] < 0.1:
        print("'train_losses1' is not between [0.1, 0.5]. Please check your answer.")
    
    elif train_losses2[-1] > 0.5 or train_losses2[-1] < 0.1:
        print("'train_losses2' is not between [0.1, 0.5]. Please check your answer.")
    
    elif test_losses1[-1] > 0.5 or test_losses1[-1] < 0.1:
        print("'test_losses1' is not between [0.1, 0.5]. Please check your answer.")
    
    elif test_losses2[-1] > 0.5 or test_losses2[-1] < 0.1:
        print("'test_losses2' is not between [0.1, 0.5]. Please check your answer.")

    elif (test_losses1[-1] - train_losses1[-1]) - (test_losses2[-1] - train_losses2[-1]) < 0.1 :
        print("'train_losses' vs. 'tests_losses' difference is not improved > 0.1. Please check your answer.")
        print("improvement: ", ((test_losses1[-1] - train_losses1[-1]) - (test_losses2[-1] - train_losses2[-1])).detach().numpy())
    
    else :
        print("\n'training_losses' are ok!")
        
    
def accuracies_check(test_accuracy1, test_accuracy2):

    print("\n\nWithout dropout")
    print("Accuracy: ", test_accuracy1[-1])
    print("\nWith dropout")
    print("Accuracy: ", test_accuracy2[-1])

    if test_accuracy1[-1] > 0.99 or test_accuracy1[-1] < 0.8:
        print("'test_accuracy1' is not between [0.8, 0.99]. Please check your answer.")
        print("'test_accuracy1' = ", test_accuracy1[-1])
    
    elif test_accuracy2[-1] > 0.99 or test_accuracy2[-1] < 0.8:
        print("'test_accuracy2' is not between [0.8, 0.99]. Please check your answer.")
        print("'test_accuracy2' = ", test_accuracy2[-1])
    else :
        print("\n'accuracies' are ok!")

