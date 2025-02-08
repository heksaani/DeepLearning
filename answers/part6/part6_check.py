import numpy as np
import pandas as pd
import torch

        
    
def test_result_check(test_loss, test_accuracy):

    print("Loss: ", test_loss)
    print("Accuracy: ", test_accuracy)

    if test_accuracy > 0.9 or test_accuracy < 0.83:
        print("'test_accuracy' is not between [0.83, 0.9]. Please check your answer.")
    
    elif test_loss > 0.5 or test_loss < 0.4:
        print("'test_loss' is not between [0.4, 0.5]. Please check your answer.")
    
    else :
        print("\nTest results are ok!")

