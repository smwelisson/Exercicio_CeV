from datetime import datetime
year = 2018
datas = dict()

datas['name'] = input("Name: ")
birth = int(input("Year of Birth: "))
datas['age'] = year - birth
datas['work_permit'] = int(input("Number of Work Permit(Zero if None): "))
if datas['work_permit'] != 0:
    datas['hiring'] = int(input("Year of Hiring: "))
    datas['salary'] = float(input("Salary: "))
    datas['retired'] = datas['age'] + (datas['hiring'] + 35 - year)
print('-=' * 30)
for k, v in datas.items():
    print(f"- {k} has value {v}")