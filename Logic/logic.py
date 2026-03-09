import sqlite3

connection = sqlite3.connect(
    "D:\\DevSpace\\Personal_Lab\\BuildZone\\Student Management\\DataBase\\database.db"
)
cursor = connection.cursor()


class AddDetails:
    def __init__(self, Table_Name: str, Details: tuple):
        self.Table_Name = Table_Name
        self.Details = Details
        self.Table_Name = getattr(self, self.Table_Name)
        self.Table_Name()

    def Student_Course(self):
        Query = """ INSERT INTO STUD_COURSE VALUES(?,?,?,?,?,?,?,?,?)"""
        cursor.execute(Query, self.Details)
        connection.commit()

    def Student_Details(self):
        Query = """ INSERT INTO STUD_DETAILS VALUES(?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(Query, self.Details)
        connection.commit()

    def Student_Performance(self):
        Result = "Fail"
        PassMark = (35 / 100) * (self.Details[5] / 6)
        if (
            self.Details[6] >= PassMark
            and self.Details[7] >= PassMark
            and self.Details[8] >= PassMark
            and self.Details[9] >= PassMark
            and self.Details[10] >= PassMark
            and self.Details[11] >= PassMark
        ):
            Result = "Pass"
        Marks_Obtained = (
            self.Details[6]
            + self.Details[7]
            + self.Details[8]
            + self.Details[9]
            + self.Details[10]
            + self.Details[11]
        )
        Percentage = Marks_Obtained / self.Details[5]
        self.Details = list(self.Details)
        self.Details[4] = Result
        self.Details[12] = Marks_Obtained
        self.Details[13] = round(Percentage*100,2)
        self.Details = tuple(self.Details)
        Query = """ INSERT INTO STUD_PERFORMANCE VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)"""
        cursor.execute(Query, self.Details)
        connection.commit()


# o = AddDetails(
#     "Student_Course",(4444,"cece","cdwce","ecc","3c3cw","wdccd","cwcwc",8,20255)

# )
class GetDetails:
    def __init__(self,Table_Name: str):
        self.Table_Name = Table_Name
        self.Table_Name = getattr(self, self.Table_Name)
        self.Table_Name()
    def Student_Course(self):
        Query = """SELECT * FROM STUD_COURSE"""
        Details = cursor.execute(Query)
        Details = Details.fetchall()
        print(Details)

    def Student_Details(self):
        Query = """SELECT * FROM STUD_DETAILS"""
        Details = cursor.execute(Query)
        Details = list(Details.fetchall())
        print(Details)
    def Student_Performance(self):
        Query = """SELECT * FROM STUD_PERFORMANCE"""
        Details = cursor.execute(Query)
        Details = list(Details.fetchall())
        print(Details)


o = GetDetails("Student_Performance")
