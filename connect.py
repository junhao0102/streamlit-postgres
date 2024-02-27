import psycopg2
import streamlit as st

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
        dbname="mydb",
        user="postgres",
        password="mysecretpassword",
        host="localhost",
        port="5432"
    )

# 创建游标对象
cursor = conn.cursor()
    
#init
def create_table():
    # 创建表
    create_sql = """
        CREATE TABLE IF NOT EXISTS data(
            name VARCHAR(20),
            phone VARCHAR(50),
            email VARCHAR(50),
            address VARCHAR(50)
        )
    """
    cursor.execute(create_sql)
    # 提交事务
    conn.commit()
    # 关闭游标和连接
    cursor.close()
    conn.close()
    print("initial successfully")
    
# 查询数据
def select(name):
    try:
        cursor.execute(f"SELECT * FROM data WHERE name = '{name}' LIMIT 1;")
        return cursor.fetchall()
    except Exception as e:
        return "Name is not exist"

# 插入数据
def insert (name, phone, email, address):
    try:
        select(name)[0] # 可能会触发异常的函数调用
        return "Name already exists"
    except Exception  as e:
        cursor.execute(f"INSERT INTO data VALUES ('{name}', '{phone}', '{email}', '{address}');")
        return "Insert successfully"
    
# 刪除数据(name為parameter)
def delete(name):
    cursor.execute(f"DELETE FROM data WHERE name = '{name}';")
    return 'delete successfully'
  
            
            
            
            
#streamlit 

st.title("Inter your information!")
#新增輸入框
name = st.text_input("Name",key="insert_name")
phone = st.text_input("Phone",key="insert_phone")
email = st.text_input("Email",key="insert_email")
address = st.text_input("Address",key="insert_address")
#按鈕
button_insert = st.button("INSERT")

#按鈕功能
if button_insert:#插入資料
    st.write(insert(name, phone, email, address))
   
   
   
   
st.title("Delete your information!")
delete_name = st.text_input("Name",key="delete_name")

#按鈕
button_delete = st.button("DELETE")

#按鈕功能
if button_delete:#刪除資料
    st.write(delete(delete_name))
    
   
    
    
    
st.title("Find your information!")
find_name = st.text_input("Name",key="find_name")
 
#按鈕    
button_SELECT = st.button("SELECT") 
#按鈕功能
if button_SELECT:#查詢資料
    st.write(select(find_name))
    
    
    
    


if __name__ == "__main__":
    create_table()