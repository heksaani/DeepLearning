import pickle
import numpy as np

with open("../answers/spacy/spacy2_data.pkl", 'rb') as file:
    # Deserialize and retrieve the variable from the file
    loaded_data = pickle.load(file)


def spacy2_check(str_to_hash, hash_to_str, text_similarity, text_bleu, filter_stop_en, filter_stop_fi,
          bananas_vector_sm, bananas_vector_lg, bananas_similarities, 
          len_stopwords_fi, five_stopwords_fi, len_stopwords_en, five_stopwords_en):

    correct_answers = 0

    
    func_output = str_to_hash(loaded_data[0])
    if func_output == loaded_data[1] :
        correct_answers += 1   
    else :
        print("\t 'str_to_hash' is not correct. Please check your answer.")

    
    func_output = hash_to_str(loaded_data[2])
    if func_output == loaded_data[3] :
        correct_answers += 1   
    else :
        print("\t 'hash_to_str' is not correct. Please check your answer.")

    
    if len(bananas_vector_sm) == len(loaded_data[4]) :
        if all(np.around(bananas_vector_sm, 3) == np.around(loaded_data[4], 3)) :
            correct_answers += 1   
        else :
            print("\t 'bananas_vector_sm' is not correct. Please check your answer.")
    else :
        print("\t 'bananas_vector_sm' is not correct. Please check your answer.")

    
    if len(bananas_vector_lg) == len(loaded_data[5]) :
        if all(np.around(bananas_vector_lg, 3) == np.around(loaded_data[5], 3)) :
            correct_answers += 1   
        else :
            print("\t 'bananas_vector_lg' is not correct. Please check your answer.")
    else :
        print("\t 'bananas_vector_lg' is not correct. Please check your answer.")

    if len(bananas_similarities) == len(loaded_data[6]) :
        for i in range(len(loaded_data[6])) : 
            bananas1 = bananas_similarities[i][1]
            bananas2 = loaded_data[6][i][1]            
            if np.around(bananas1, 4) == np.around(bananas2, 4) :
                if i == len(loaded_data[6])-1 :
                    correct_answers += 1   
            else :
                print("\t 'bananas_similarities' is not correct. Please check your answer.")
    else :
        print("\t 'bananas_similarities' is not correct. Please check your answer.")

    
    func_output = text_similarity(loaded_data[7], loaded_data[8])
    if np.around(func_output, 3) == np.around(loaded_data[9], 3) :
        correct_answers += 1   
    else :
        print("\t 'text_similarity' is not correct. Please check your answer.")

    
    func_output = text_bleu(loaded_data[7], loaded_data[8])
    if np.around(func_output.score, 4) == np.around(loaded_data[10].score, 4) :
        correct_answers += 1   
    else :
        print("\t 'text_bleu' is not correct. Please check your answer.")

    
    if len_stopwords_fi == loaded_data[11] :
        correct_answers += 1   
    else :
        print("\t 'len_stopwords_fi' is not correct. Please check your answer.")

    
    from spacy.lang.fi.stop_words import STOP_WORDS
    if (all(x in STOP_WORDS for x in five_stopwords_fi)) :
        correct_answers += 1   
    else :
        print("\t 'five_stopwords_fi' is not correct. Please check your answer.")

    
    if len_stopwords_en == loaded_data[12] :
        correct_answers += 1   
    else :
        print("\t 'len_stopwords_en' is not correct. Please check your answer.")

    
    from spacy.lang.en.stop_words import STOP_WORDS
    if (all(x in STOP_WORDS for x in five_stopwords_en)) :
        correct_answers += 1   
    else :
        print("\t 'five_stopwords_en' is not correct. Please check your answer.")

    
    func_output = filter_stop_en(loaded_data[13])
    if func_output == loaded_data[14] :
        correct_answers += 1   
    else :
        print("\t 'filter_stop_en' is not correct. Please check your answer.")

    
    func_output = filter_stop_fi(loaded_data[15])
    if func_output == loaded_data[16] :
        correct_answers += 1   
    else :
        print("\t 'filter_stop_fi' is not correct. Please check your answer.")
    

    return correct_answers 
