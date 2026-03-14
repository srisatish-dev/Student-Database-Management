import sqlite3

connection = sqlite3.connect(
    "D:\\DevSpace\\Personal_Lab\\BuildZone\\Student Management\\DataBase\\database.db"
)
cursor = connection.cursor()



class AddDetails:
    def __init__(self, Table_Name: str, Details: tuple):
        self.Details = Details
        self.Table_Name = Table_Name
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


class GetDetails:
    def __init__(self,Table_Name: str):
        self.Table_Name = Table_Name
        self.Table_Name = getattr(self, self.Table_Name)
        self.Table_Name()
        connection.commit()
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

class SearchDetails:

    def __init__(self, Table_Name: str, ID_list: tuple):
        self.Id_list = ID_list
        self.Table_Name = Table_Name
        self.Table_Name = getattr(self, self.Table_Name)
        self.Details_list = []
        for self.id in self.Id_list:
            self.Details_list.append(self.Table_Name(self.id))
            # print(self.id)
        print(self.Details_list)
        connection.commit()

    def Student_Course(self,id):
        Query = f"""SELECT * FROM STUD_COURSE WHERE STUD_ID={id}"""
        Details = cursor.execute(Query)
        Details = Details.fetchone()
        return(Details)

    def Student_Details(self,id):
        Query = f"""SELECT * FROM STUD_DETAILS WHERE STUD_ID = {id}"""
        Details = cursor.execute(Query)
        Details = Details.fetchone()
        return(Details)
    def Student_Performance(self,id):
        Query = f"""SELECT * FROM STUD_PERFORMANCE WHERE STUD_ID = {id}"""
        Details = cursor.execute(Query)
        Details = Details.fetchone()
        return(Details)

class DelDetails:
    def __init__(self,Table_Name: str, ID_list: tuple):
        self.Id_list = ID_list
        self.Table_Name = Table_Name
        self.Table_Name = getattr(self,self.Table_Name)
        for self.id in self.Id_list:
            self.Table_Name(self.id)
        connection.commit()
    def Student_Course(self,id):
        Query = f"""DELETE FROM STUD_COURSE WHERE STUD_ID = {id};"""
        cursor.execute(Query)

    def Student_Details(self, id):
        Query = f"""DELETE FROM STUD_DETAILS WHERE STUD_ID = {id};"""
        cursor.execute(Query)

    def Student_Performance(self, id):
        Query = f"""DELETE FROM STUD_PERFORMANCE WHERE STUD_ID = {id};"""
        cursor.execute(Query)
        
        
O = DelDetails("Student_Course",())
