# Jason Luis 
# Professor Ghaforyfard
# March 4, 2024 
# Using For loop, write a program to ask for the name, salary, and the state for 6 employees. Calculate the federal tax, state tax, and the net salary for each employee. 
# If the salary is greater than 100,000 then calculate the federal tax at 20 percent. Otherwise calculate the federal tax at 15%. 
# If the employee is from CA, NV, AZ, or TX calculate the state tax at 10%. Otherwise calculate the state tax at 12%. 
# To calculate the net salary, subtract the federal and state tax from the gross salary. 


#inputs 
from cmath import e


numofemployees = input("How many employees are there?: ") 

intnumofemployees = int(numofemployees)

#FOR Loops and If Conditions

for i in range(intnumofemployees):

    employee = input("\nWhat is your name?: ") 

    salary = float(input("\nWhat is your salary?(ONLY numbers): ")) 

    states = input("\nWhat state do you live in? (Please put the state's abbreviation; ex: CA (California): ").upper() 

    if salary >= 100000:
        
        federal_tax = salary * 0.20

        print("\nFederal Tax: $", federal_tax) 

    else:

        federal_tax = salary * 0.15

        print("\nFederal Tax: $",federal_tax)

    
    if states.upper() in ['CA','NV','AZ','TX']:

        state_tax = float(salary) * 0.10 

        net_salary = float(salary) - float(federal_tax) - float(state_tax)

        print("\nState Tax: $", state_tax, "\n\nNet Salary: $", net_salary) 

        print("\n===================================================")

    else:

        state_tax = float(salary) * 0.12

        net_salary = float(salary) - float(federal_tax) - float(state_tax)

        print("\nState Tax: $", state_tax, "\n\nNet Salary: $", net_salary)

        print("\n===================================================")
