from datetime import datetime
from crewai import Task

class AICoderTasks():

    def task_data_preprocess(self,agent,df,uploaded_file,predictvar):
        return Task(
            description="""Think of what kinds of data cleaning and data processing and feature engineering steps
            are required and jot down all of this in a coding flow plan ;

            Here is a sample of the user's data:
                    {df}
            The file name is called {uploaded_file}
            The variable to predict is {predictvariable}
            The variable data types are {dtypes}
            Stick only to the phases like encoding categorical variables, feature scaling, and selection 
            and more in feature engineering and more in data preprocessing , REMEMBER do not go beyond that TO  like  model_building , hp_tuning etc. 

            Code your plan and pass all of this to model_building_agent

                """.format(df=df.head(50),uploaded_file=uploaded_file,predictvariable=predictvar,dtypes=df.dtypes),
            agent=agent,
            expected_output="""A coding flow with correct data preprocessing and feature engineering steps based on the 
            data given ."""
            )

    def task_choose_model(self,agent,df,uploaded_file,predictvar,context):
        return Task(
                    description="""
                    Build a AI coding flow on the next phases after data_preprocessing like model_building , model_evaluation ,hp_tuning and
                    .... etc(in a structure/format similar to data_preprocessing flow) to solve the problem based on the data {df} 
                    and the variable to be predicted {predictvariable}.
                    The variable data types are {dtypes}
    
                    The file name is called {uploaded_file}
                    Pass the entire code , The code output provided by data_preprocessing_agent and the entire code that you generated
                    """.format(df=df.head(),uploaded_file=uploaded_file,predictvariable=predictvar,dtypes=df.dtypes),
                    agent=agent,
                    expected_output=""" The entire code output provided  + the entire code that 
                    you generated (on the next phases after data_preprocessing""",
                    context=context
                )

    def task_check_code(self,agent,context):       

            return Task(
            description="""Check the entire code provided by model_building_agent , assessing the steps coding flow and fixing any and all types of error""",
            agent=agent,
            expected_output="""The entire code provided , that has been revised by the and is free of any errors or 
            issues identified during the validation process. """,
            context=context
            )