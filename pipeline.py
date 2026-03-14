import pandas as pd
import sqlite3

data = pd.read_csv("students.csv")

data = data.dropna()

data["average_score"] = (
    data["math_score"] +
    data["english_score"] +
    data["science_score"]
) / 3

conn = sqlite3.connect("students.db")

data.to_sql("students_clean", conn, if_exists="replace", index=False)

print("Data pipeline completed successfully")

conn.close()
