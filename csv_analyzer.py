#import pandas and json
import pandas as pd 
import json

#function to read csv file and return a dataframe  
def read_csv(filename):
    return pd.read_csv(filename)

df= read_csv("students.csv")
print(df)

#count total students

total_students = int(len(df))
print("Total students:", total_students)

#count students by country
students_by_country = df["country"].value_counts()
print("Students by country:")
print(students_by_country)  

#count completed bet_status
completed_bets = (df["bet_status"] == "completed").sum()
completed_bets = int(completed_bets)
print("Completed bets:", completed_bets)

#calculate completion rate
if total_students > 0:
    completion_rate = round((completed_bets / total_students) * 100, 2)  
    print(f"Completion rate: {completion_rate:.2f}%")
else:
    print("No students found.")

#store results in a dictionary
results = { 
    "total_students": int(total_students),
    "students_by_country": students_by_country.to_dict(),
    "completed_bets": int(completed_bets),
    "completion_rate": completion_rate
}   

#save dictionary to json file
with open("results.json", "w") as json_file:
    json.dump(results, json_file, indent=4)
print("Results saved to results.json")