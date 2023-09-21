import pandas as pd

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
        
        email = f"{first_name[0].lower()}{surname.lower()}@gmail.com"

        return email



# Create a function to create a list of emails from a list of names
def create_email_list(excel_file):
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

    