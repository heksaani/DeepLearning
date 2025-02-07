import numpy as np
import pandas as pd
import torch

def training_losses_check(training_losses):

    print("\n", training_losses)
    
    if len(training_losses) != 5 :
        print("'training_losses' lenght is not correct. Please check your answer.")
    
    elif training_losses[0] > 3 or training_losses[0] < 1.2 :
        print("'training_losses' first element is not on correct level. Please check your answer.")

    elif training_losses[4] > 0.5 or training_losses[4] < 0.2 :
        print("'training_losses' last element is not on correct level. Please check your answer.")

    else :
        print("'training_losses' is ok!")
    
def probabilities_check(ps):

    print("\n", ps)

    if len(ps.detach().numpy()[0]) != 10 :
        print("'probabilities' lenght is not correct. Please check your answer.")
    
    elif np.around(sum(ps.detach().numpy()[0]), 2) != 1.0:
        print("'probabilities' does not sum to 1. Please check your answer.")

    else :
        print("'probabilities' is ok!")

