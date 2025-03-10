import pandas as pd

def csv():
    print("1. Read complete csv file")
    print("2. Reading file without index")
    print("3. Sorting data as per your choice ")
    print("4. Read Top and Bottom Records as per your choice")
    print("5. Read file with specified columns")
csv()

def read_csv():
    print("Reading Data From csv")
    print(" ")
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print(df)


def no_index():
    print("Reading Data From csv file without index values")
    print(" ")
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", index_col=0)
    print(df)


def data_sorting():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print(">> To display record in Descending Order")
    print("Press 1 to arrange the record as per     TOTAL CASES")
    print("Press 2 to arrange the record as per    TOTAL DEATHS")
    print("Press 3 to arrange the record as per    ACTIVE CASES")
    print("Press 4 to arrange the record as per TOTAL RECOVERED")
    print(">> To display record in Ascending Order")
    print("Press 5 to arrange the record as per     TOTAL CASES")
    print("Press 6 to arrange the record as per    TOTAL DEATHS")
    print("Press 7 to arrange the record as per    ACTIVE CASES")
    print("Press 8 to arrange the record as per TOTAL RECOVERED")

    sr = int(input("Enter Your Choice : "))

    print(" ")

    if sr == 1:
        df1 = df.sort_values(by=["Total Cases"], ascending=[False])
        print(df1)
    elif sr == 2:
        df1 = df.sort_values(by=["Active Cases"], ascending=[False])
        print(df1)
    elif sr == 3:
        df1 = df.sort_values(by=["Total Deaths"], ascending=[False])
        print(df1)
    elif sr == 4:
        df1 = df.sort_values(by=["Total Recovered"], ascending=[False])
        print(df1)
    elif sr == 5:
        df1 = df.sort_values(by=["Total Cases"])
        print(df1)
    elif sr == 6:
        df1 = df.sort_values(by=["Active Cases"])
        print(df1)
    elif sr == 7:
        df1 = df.sort_values(by=["Total Deaths"])
        print(df1)
    elif sr == 8:
        df1 = df.sort_values(by=["Total Recovered"])
        print(df1)
    else:
        print("       ####### Enter a valid input #######       ")

def read_top_and_bottom():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print("Press 1 to extract records from top")
    print("Press 2 to extrcat records from bottom")

    ch = int(input("Enter your choice : "))

    if ch == 1:
        top = int(input("Enter How Many Records You want To Display From Top : "))
        df1 = df.head(top)
        print(df1)
    elif ch == 2:
        bottom = int(input("Enter How Many Records You want To Display From Bottom : "))
        df2 = df.tail(bottom)
        print(df2)
    else:
        print("       ####### Enter a valid input #######       ")


def read_specified_col():
    df = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
    print("Press 1 to print COUNTRIES & VACCINATION RATE")
    print("Press 2 to print COUNTRIES & DEATH RATE")
    print("Press 3 to print COUNTRIES & RECOVERY RATE")
    print("Press 4 to print INDIA's COVID ANALYSIS ")
    print("Press 5 to print COUNTRIES & ACTIVE CASES")
    print("Press 6 to print COUNTRIES & TOTAL DEATHS")
    print("Press 7 to print COUNTRIES & TOTAL TESTS")
    print("Press 8 to print COUNTRIES HAVING 60% & ABOVE RECOVERY RATE")

    rs = int(input("Enter your choice : "))

    print(" ")

    if rs == 1:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Vaccines Rate"])
        print(df1)
    elif rs == 2:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Death Rate"])
        print(df1)
    elif rs == 3:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Recovery Rate"])
        print(df1)
    elif rs == 4:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
        ind = df1.iloc[1]
        print(ind)
    elif rs == 5:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Active Cases"])
        print(df1)
    elif rs == 6:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Total Deaths"])
        print(df1)
    elif rs == 7:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv", usecols=["Country", "Total Tests"])
        print(df1)
    elif rs == 8:
        df1 = pd.read_csv(r"C:\Users\dell\Desktop\dataset.csv")
        mvp = df1[df1["Recovery Rate"] > 60]
        print(mvp)
    else:
        print("       ####### Enter a valid input #######       ")


op = int(input("Enter your choice : "))
if op == 1:
    read_csv()
elif op == 2:
    no_index()
elif op == 3:
    data_sorting()
elif op == 4:
    read_top_and_bottom()
elif op == 5:
    read_specified_col()
else:
    print("       ####### Enter a valid input #######       ")