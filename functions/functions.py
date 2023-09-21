import pandas as pd
import numpy as np
import tensorflow as tp
from transformers import BertTokenizer, TFBertModel

# def load_labse_model():
#     try:
#         tokenizer = BertTokenizer.from_pretrained("sentence-transformers/LaBSE")
#         model = TFBertModel.from_pretrained("sentence-transformers/LaBSE", force_download=True, resume_download=False)
#         return tokenizer, model
#     except OSError as e:
#         print(f"Error loading LaBSE model: {e}")
#         return None, None


def process_file(excel_file):
    
    # Initialize the LaBSE model and tokenizer
    # tokenizer, model = load_labse_model()
    # if tokenizer is None or model is None:
    #     return []
    
    

    # # Create a function to encode a sentence into a tensor
    # def sent_encode(sent):
    #     return tokenizer.encode_plus(sent, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True)
    #     #         print('Sentence:', sent)
    #     #         print('Encoded:', tokenizer.encode_plus(sent, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True))
    #     #         print('Decoded:', tokenizer.decode(tokenizer.encode_plus(sent, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True)['input_ids']))
    #     #         print('')
    # # Create a function to encode a sentence pair into a tensor
    # def pair_encode(sent1, sent2):
    #     return tokenizer.encode_plus(sent1, sent2, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True)
    #     #         print('Sentence 1:', sent1)
    #     #         print('Sentence 2:', sent2)
    #     #         print('Encoded:', tokenizer.encode_plus(sent1, sent2, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True))
    #     #         print('Decoded:', tokenizer.decode(tokenizer.encode_plus(sent1, sent2, add_special_tokens=True, max_length=128, padding=True, return_attention_mask=True, truncation=True)['input_ids']))
    #     #         print('') 

    # Create a function to create an email from the first letter of first name and surname
    def create_email(student_name):
        student_names = student_name.split(", ")
        if len(student_names) >= 2:
            first_name = student_names[1]
            surname = student_names[0]
        else:
            first_name = student_names[0]
            surname = ''
        
        first_name  = ''.join(e for e in first_name if e.isalnum())
        surname = ''.join(e for e in surname if e.isalnum())
    # print('First name:', first_name)
    # print('Surname:', surname)
    # print('Email:', first_name[0].lower() + '.' + surname.lower() + '@gmail.com')
        
        email = f"{first_name[0].lower()}{surname.lower()}"

        return email
                
    # Create a function to create a list of emails from a list of names
    def create_email_list():
        try:
            df = pd.read_excel(excel_file)
            print('Excel file is successfully opened')
        except Exception as e:
            print(f"Error loading excel file: {e}")
            return None
            
        email_list = []

        for student_name in df['Student Name']:
                
                # embeddings = tokenizer(student_name, return_tensors="tf", padding=True, truncation=True)
                email_list.append(create_email(student_name))
                unique_emails = []
                seen_emails = set()
                for email in email_list:
                    while email in seen_emails:
                        email += str(np.random.randint(10))
                    unique_emails.append(email)
                    seen_emails.add(email)
                return unique_emails
                # print('Student names:', student_names)
                # print('Email list:', email_list)

    
   
