def CalculateTaxesOnSalary(salary):
    if salary >= 30000:
        return salary * 0.33
    if salary < 15000:
        return salary * 0.12        
    if salary < 30000:
        return salary * 0.28        

x = CalculateTaxesOnSalary(45000)        