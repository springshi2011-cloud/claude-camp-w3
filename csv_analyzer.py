#import pandas and json
import pandas as pd 
import json

#function to read csv file and return a dataframe 
def read_csv(filename):
    df = pd.read_csv(filename)
    df.columns = df.columns.str.strip() 
    return df

def analyze_students(df):   
    total_students = len(df)
    students_by_country = df["country"].value_counts()
    completed_bets = int(
        (df["bet_status"].str.lower().str.strip() == "completed").sum()
        )
    if total_students > 0:
        completion_rate = round((completed_bets / total_students) * 100, 2)     
    else:
        completion_rate = 0.0

    results = { 
        "total_students": int(total_students),
        "students_by_country": students_by_country.to_dict(),
        "completed_bets": int(completed_bets),
        "completion_rate": completion_rate
    }   
    return results

def save_report(report, filename="report.json"):
    with open(filename, "w") as json_file:
        json.dump(report, json_file, indent=4, ensure_ascii=False)

#main function 
def main():
    df= read_csv("students.csv")
    df.columns = df.columns.str.strip()
    report = analyze_students(df)
    print(report)
    save_report(report, "report.json")
    print("Report saved to report.json")

#call main function
if __name__ == "__main__":    
    main()
