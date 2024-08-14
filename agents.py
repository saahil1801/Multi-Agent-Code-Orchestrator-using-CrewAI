from crewai import Agent

class AICoderAgents():

    def datapreprocessing(self,llm):
        return Agent(
            role='Data_Preprocessing_Agent',
            goal="""Create a coding flow plan of the kinds of data cleaning and data processing and feature engineering steps
            are required and jot down all of this in a coding flow plan.
            
            """,
            backstory="""Expert in data cleaning , data preprocessing and feature engineering required for ML and AI coding.""",
            verbose=True,
            allow_delegation=False,

            memory=True,
            max_iter=7,
            llm=llm

        )
    def modelbuilding(self,llm):
        return Agent(
            role='Model_Building_Agent',
            goal="""Design a codeflow on the next phases after datapreprocessing like model building,
            model evaluation etc. """,
            backstory="""You are an expert in AI coding , including having strong coding knowledge of
            various branches like ML , DL, NLP and using LLMS also which you use depending on the problem .
            You know what to code , based on the data given.""",
            verbose=True,
            allow_delegation=False,
        
            memory=True,
            llm=llm
    
        )
    def validator_agent(self,llm):
        return Agent(
            role='Validator_Agent',
            goal="""Check the entire AI coding flow provided throughly 
            assessing the steps coding flow.You need to make sure the steps in coding flow are correct by fixing the all 
            kinds of errors in the flow by making changes wherever necessary and  finally printing the entire corrected code""",
            backstory="""You have strong AI coding knowledge of various branches like ML , DL, NLP , LLMS .
            You are an expert in evaluating , validating and correcting AI coding flows. """,
            verbose=True,
            allow_delegation=False,
            llm=llm
    
        )
