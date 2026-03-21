def replace_domain(email,old_domain,new_domain):
    if "@" + old_domain in email:
        print("your old email is:", email)
        index = email.index('@' + old_domain)
       
        new_email = email[:index] + '@' + new_domain
        print ("your new email is:", new_email)
    
    return new_email

replace_domain('hamada.alhebshi@qq.com','qq.com','gmail.com')    
