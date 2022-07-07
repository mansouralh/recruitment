


skills=["Python","C++","Javascript","Juggling", "Running","Eating"]

def get_skills():
    # Add at least 3 random skills for the user to select from
    skills=["Python","C++","Javascript","Juggling", "Running","Eating"]
    return skills


def show_skills(skills):
    # Pretty print skills to the user
    # Write your code here
    print("Skills:")
    # skills_list=[]
    for count, skills in enumerate(skills, start=1):
        
        print (count,skills)
    #     skills_list.append(count, skills)
    # print (skills_list())
    # print("234")
    # count, skills

def get_user_skills(skills):
    # Show the available skills and have user pick from them
    # Write your code here
    
    show_skills(skills)
    skill1=input("Choose a skill from above by entering its number:")
    skill2=input("Choose another skill from above by entering its number:")
    # skill11=[skills[int(skill1)]]
    # print(skill11)
    
    user_skills=[skills[int(skill1)-1],skills[int(skill2)-1]]
    
    return(user_skills)
    
        #  skills_list.append = (count, skills)
    # print (skills_list)
    # input(f" choose two skills from the list {skills_list()}")
    # skills_list.append= input(skills) 
    # return skills_list
def get_user_cv(skills):
    # Get the users CV from their inputs
    # Write your code here
    user_input =get_user_skills(skills)
    
    cv_dictionary= {'name': input("enter your name :"),'age':input("enter your age pleasssse:"),'experience':input("please enter years of experience"), "skills": user_input }
 

   
    print (cv_dictionary)
    return cv_dictionary
def check_acceptance(cv):
    # Check if the cv is acceptable or not and return a boolean based on that
    # Write your code here
    # bool 25>('age' in cv_dictionary) >40: 

    print ("Welcome to the recruitment program")
    
    cv = get_user_cv(skills)
    desired_skill=["C++","Python"]
   
    if ('age' in cv) >25 and ('age' in cv) <40 and ('experience' in cv) >3 and (desired_skill in ('skills' in cv)):
        
        print ("you're accepted ")
    else: 
        print ("go out")
    
        
    
      
def main():
    # Write your main logic here by combining the functions above into the
    # desired outcome
    ...
check_acceptance( get_skills())
# get_user_skills(get_skills())
# print (get_skills())

if __name__ == "__main__":
    main()
