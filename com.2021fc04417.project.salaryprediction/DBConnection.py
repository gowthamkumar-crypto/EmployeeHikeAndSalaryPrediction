import psycopg2

con = psycopg2.connect(user="postgres",password="password",
                       host="localhost",database="EHSA_e0",
                       port = "5432")




def getLevelIdByRoleNameAndLevel(role_id,level):
    cursor = con.cursor()
    statement = "select level_id from levels where role_id="+str(role_id)+" and level="+str(level)+";"
    cursor.execute(statement)
    response = cursor.fetchone()[0]
    cursor.close()
    return response

def getRoleIdByRoleName(role):
    cursor = con.cursor()
    statement = "select role_id from roles where role_name=\'"+str(role)+"\';"
    cursor.execute(statement)
    response = cursor.fetchone()[0]
    cursor.close()
    return response



def saveCandiate(record, role_id, level_id, predictedSalary):
    cursor = con.cursor()
    col = ['First Name','Last Name','Age','Years of Experience','Email','gender', 'Location','Prev Salary','Education Level']
    statement = "INSERT INTO public.candidate(candidate_first_name, candidate_last_name, age, experience, email, gender, location, prev_salary, education, role_id, level_id,salary_predicted) VALUES ("
    values=""
    for c in col:
        if(c not in ['Age','Years of Experience','Prev Salary']):
            if(record[c]=='Masters\'s' and c=='Education Level'):
                values = values+"'Masters',"
            elif(record[c]=='Bachelor\'s' and c=='Education Level'):
                values = values + "'Bachelors',"
            else:
                values = values + "'" + str(record[c]) + "',"
        else:
            values = values+str(record[c]) + ","
    values = values+str(role_id) + "," + str(level_id) +"," +str(predictedSalary)+") RETURNING cid;"
    insertStatement = statement+values
    cursor.execute(insertStatement)
    con.commit()
    response = cursor.fetchone()[0]
    cursor.close()
    return response

def getRoles():
    rolesList = []
    cursor = con.cursor()
    statement = "SELECT role_name FROM roles;"
    cursor.execute(statement)
    response = cursor.fetchall()
    cursor.close()
    for r in response:
        rolesList.append(r[0])
    return rolesList

def getEmployeeReviewDetails(empId):
    cursor = con.cursor()
    statement = "SELECT total_working_hours,actual_working_hours,job_involvement, over_time, assigned_story_points, spill_over_story_points, achivements, core_values FROM sprint_review where emp_id="+str(empId)+";"
    cursor.execute(statement)
    response = cursor.fetchall()
    cursor.close()
    return response
