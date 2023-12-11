import mysql.connector
conn_obj=mysql.connector.connect(host='localhost',
                                 username='root',
                                 password='1234',
                                 database='ToDo')

if conn_obj:
    print("successfully connected")
else:
    print('try again')

cur_obj=conn_obj.cursor()
 
 #user define function
def create_table():
    cur_obj.execute("CREATE TABLE if not exists taskTable(task LONGTEXT,task_status TEXT,task_due_date DATE)")

def add_data(task,task_status,task_due_date):
    cur_obj.execute("INSERT INTO taskTable(task,task_status,task_due_date) VALUES(%s,%s,%s)",(task,task_status,task_due_date))
    conn_obj.commit()



def read_all():
    cur_obj.execute("SELECT * FROM toDo.taskTable")
    result=cur_obj.fetchall()
    return result

def get_task(task):
    cur_obj.execute('SELECT * FROM taskTable WHERE task="{}"'.format(task))
    result=cur_obj.fetchall()
    return result

def edit_data(n_task,n_task_status,n_task_due_date,task,task_status,task_due_date):
    cur_obj.execute("UPDATE taskTable SET task=%s,task_status=%s,task_due_date=%s WHERE task=%s and task_status=%s and task_due_date=%s",(n_task,n_task_status,n_task_due_date,task,task_status,task_due_date))
    conn_obj.commit
    data= cur_obj.fetchall()
    return data

def view_unique_task():
    cur_obj.execute('SELECT DISTINCT task FROM taskTable')
    data=cur_obj.fetchall()
    return data

def delete_data(task):
    cur_obj.execute('DELETE FROM taskTable WHERE task="{}"'.format(task))
    conn_obj.commit()
