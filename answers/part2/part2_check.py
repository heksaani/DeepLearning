import numpy as np
import pandas as pd
import torch

[output1_shape_t, softmax_input_t, softmax_output_t, error_input1_t, error_input2_t, error_output_t] = torch.load('../answers/part2/tensor_data.pt')


def part2_shape_check(output1_shape):

    correct_answers = 0 
    print(output1_shape)
    
    # output1
    if output1_shape_t == output1_shape :
        correct_answers += 1   
    else :
        print("\t 'output1.shape' is not correct. Please check your answer.")

    return correct_answers 


    
def softmax_func_check(softmax_func):

    correct_answers = 0
    func_output = softmax_func(softmax_input_t)

    if torch.equal(torch.round(func_output, decimals=3), torch.round(softmax_output_t, decimals=3)) :
        correct_answers += 1   
    else :
        print("\t 'softmax_func' is not correct. Please check your answer.")

    return correct_answers 
    

def error_func_check(error_func):

    correct_answers = 0
    func_output = error_func(error_input1_t, error_input2_t)

    if torch.equal(torch.round(func_output, decimals=3), torch.round(error_output_t, decimals=3)) :
        correct_answers += 1   
    else :
        print("\t 'error_func' is not correct. Please check your answer.")

    return correct_answers 


def part2_model_check(model):

    correct_answers = 0    
    
    # model
    reloaded = torch.load('../answers/part2/part2_model.pt')
    print(model)
    
    if str(reloaded) == str(model) :
        correct_answers += 1   
    else :
        print("\t 'model' is not correct. Please check your answer.")

    return correct_answers 
    

def part2_sequential_model_check(sequential_model):

    correct_answers = 0    
    
    # model
    sequential_reloaded = torch.load('../answers/part2/part2_sequential_model.pt')
    print(sequential_model)
    
    if str(sequential_reloaded) == str(sequential_model) :
        correct_answers += 1   
    else :
        print("\t 'sequential_model' is not correct. Please check your answer.")
    
    return correct_answers 
