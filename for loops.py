for i in range(1,11):
    print(f"7 x {i} ={7*i}")

stars pattern
for i in range(1,6):
    print("*"*i)

# CONTINUE BREAK AND PASS 
names=['pavan','kiran',' ','surendra']
for name in names:
    if name==' ':
        break
    print(f"Name = {name}")

names=['pavan','kiran',' ','surendra']
for name in names:
    if name==' ':
        continue
    print(f"Name = {name}")

names=['pavan','kiran',' ','surendra']
for name in names:
    if name==' ':
        name = name.replace(' ','unknown')
    print(f"Name = {name}")

for else
files = ['student.csv','parent.csv','lecturer.txt','guardian.csv']
for file in files:
    if file == 'lecturer.txt':
        break
    print(file)
else:
    print("there are txt files")

for else 2
files=['report.csv','data.xlsx','summary.docx','report.csv','data.csv']
seen=[]
for file in files:
    if file in seen:
        print("duplicate is found")
        break
    seen.append(file)
else:
    print("all files are unique")

#nested loops
for x in range(3):
    for y in range(2):
        print(f"({x},{y})")

colors = ['red','black','blue','grey']
sizes = ['L','M','S','XL','XXL']
for color in colors:
    for size in sizes:
        print(f'{color} - size {size}')

years=['2025','2026']
months=['jan','feb']
dates=range(1,29)
for y in years:
    for m in months:
        for d in dates:
            print(f"reported {y} {m} {d}")   
  
tables = ['customers','orders','products','prices']
columns = ['id','create_date']
for t in tables:
    for c in columns:
        print(f"select count(*) FROM {t} WHERE {c} IS NULL")


for i in range(1,6):
    for j in range(1,6):
        print(i,j)

for i in range(6):
    for j in range(6):
        print(j, end=" ")
    print()

files = ['report.csv', 'data.xlsx', 'summary.docx', 'report.csv', 'data.csv']

seen = []

for file in files:
    if file in seen:
        print("Duplicate found")
        break
    seen.append(file)

else:
    print("All files are unique")
#reverse a string
text = 'python'
reverse = ""

for ch in text:
    reverse = ch + reverse
print(reverse) 











    