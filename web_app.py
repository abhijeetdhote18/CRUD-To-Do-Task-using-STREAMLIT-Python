import streamlit as st
import pandas as pd
from db_function import *
import plotly.express as px

st.title('WELCOME TO DO APPLICATION USING STREAMLIT')                           # Title on web page
ch=['Create','Read','Update','Delete','About']                                  # choice options List
option = st.sidebar.selectbox('Select Section',ch)                              # side bar with select box with given choice option

# if Create is selected
if option=='Create':
    create_table()                                                              # Function called from db_function
    st.subheader('Add Records')
    col1,col2=st.columns(2)
    with col1:
        task=st.text_area("To Do Task")
    with col2:
        task_status=st.selectbox("Status",['ToDo','Doing',"Done"])
        task_due_date=st.date_input("Due Date")
    if st.button("Add Record"):
        add_data(task,task_status,task_due_date)
        st.success("Record Added sucessfully")

# if Read is Selected
elif option=='Read':
    st.subheader('View Records')
    res=read_all()                                                               # Function called from db_function
    df=pd.DataFrame(res,columns=['Task','Task Status','Task Due Date'])
    with st.expander("View Records"):
        st.dataframe(df)
    with st.expander('Task Status'):
        task_df=df['Task Status'].value_counts().to_frame()
        st.write(task_df)

        task_df=task_df.reset_index()
        

        p1=px.pie(task_df,names='Task Status',values='count')
        st.plotly_chart(p1)

    
# if Update is selected
elif option=='Update':
    st.subheader('Update Records')
    res=read_all()                                                                # Function called from db_function
   
    df=pd.DataFrame(res,columns=['Task','Task Status','Task Due Date'])
    with st.expander("View Records"):
        st.dataframe(df)
    
    list_of_task= [i[0] for i in view_unique_task()]                              # Function called from db_function
    
    selected_task=st.selectbox('Task To Edit',list_of_task)
    selected_result=get_task(selected_task)                                       # Function called from db_function
   
    if selected_result:
        task=selected_result[0][0]
        task_status=selected_result[0][1]
        task_due_date=selected_result[0][2]
        col1,col2=st.columns(2)
        with col1:
            n_task=st.text_area("To Do Task",task)
        with col2:
            n_task_status=st.selectbox("Status",['ToDo','Doing',"Done"])
            n_task_due_date=st.date_input("Due Date",task_due_date)
        if st.button("update Record"):
            edit_data(n_task,n_task_status,n_task_due_date,task,task_status,task_due_date)    # Function called from db_function
            st.success("Record Added sucessfully")
    res2=read_all()                                                                      # Function called from db_function
    df=pd.DataFrame(res2,columns=['Task','Task Status','Task Due Date'])
    with st.expander("View Records"):
        st.dataframe(df)

# if Delete is Selected
elif option=='Delete':
    st.subheader('Remove Records')
    res=read_all()
    
    df=pd.DataFrame(res,columns=['Task','Task Status','Task Due Date'])
    with st.expander("View Records"):
        st.dataframe(df)
   
    list_of_task= [i[0] for i in view_unique_task()]
    
    selected_task=st.selectbox('Task To Edit',list_of_task)
    st.warning("Do you want to Delete :: {}".format(selected_task))
    if st.button('Yes'):
        delete_data(selected_task)
        st.success("Selected task is deleted successfully {}".format(selected_task))
    res2=read_all()
    
    df=pd.DataFrame(res2,columns=['Task','Task Status','Task Due Date'])
    with st.expander("View Records"):
        st.dataframe(df)


elif option=='About':
    st.subheader('Project Information: Project on To Do List using STREAMLIT Module.\nStart Date : 06-11-2023, End Date : 09-11-2023 with help of mentor Deepali mam by Abhijeet Dhote.')


#Note - run this in Terminal :> streamlit run webapp.py 
