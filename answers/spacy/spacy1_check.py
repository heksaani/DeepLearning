import pickle

with open("../answers/spacy/spacy1_data.pkl", 'rb') as file:
    # Deserialize and retrieve the variable from the file
    loaded_data = pickle.load(file)

def spacy1_check(return_verbs, return_lemmas, return_places, wikipedia_search):

    correct_answers = 0
    
    func_output = return_verbs(loaded_data[0])
    if func_output == loaded_data[1] :
        correct_answers += 1   
        print("\n")
    else :
        print("\t 'return_verbs' is not correct. Please check your answer.")

    func_output = return_lemmas(loaded_data[2])
    if func_output == loaded_data[3] :
        correct_answers += 1   
        print("\n")
    else :
        print("\t 'return_lemmas' is not correct. Please check your answer.")

    func_output = return_places(loaded_data[4])
    if func_output == loaded_data[5] :
        correct_answers += 1   
        print("\n")
    else :
        print("\t 'return_places' is not correct. Please check your answer.")

    func_output = wikipedia_search(loaded_data[6])
    if func_output == loaded_data[7] :
        correct_answers += 1   
        print("\n")
    else :
        print("\t 'wikipedia_search' is not correct. Please check your answer.")

    
    return correct_answers 
