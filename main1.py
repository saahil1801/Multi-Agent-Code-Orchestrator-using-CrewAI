import streamlit as st
import pandas as pd
import os
from crewai import Agent, Task, Crew , Process
from langchain_ollama import ChatOllama
from langchain_groq import ChatGroq
from langchain.chains import ConversationChain
from agents import AICoderAgents
from tasks import AICoderTasks


    
def main():

    # Set up the customization options
    st.sidebar.title('Customization')
    

    # llm = ChatGroq(
    #         temperature=0, 
    #         groq_api_key = "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", 
    #         model_name=model
    #     )

    llm = ChatOllama(
    model = "llama3.1")
    #ollama pull llama3.1
    #ollama run llama3.1
    
    # Streamlit UI
    st.title('CrewAI Machine Learning Assistant')
    multiline_text = """
    This Machine Learning Assistant is designed to guide users through the process of defining, 
    assessing, and solving machine learning problems. 
    """

    st.markdown(multiline_text, unsafe_allow_html=True)

    

    uploaded_file = st.file_uploader("Upload a sample .csv of your data (optional)")
    execute=st.button("Execute")
    if uploaded_file is not None:
        try:
            # Attempt to read the uploaded file as a DataFrame
            df = pd.read_csv(uploaded_file)
            variable_names = df.columns.tolist()
            predictvar = st.sidebar.selectbox("Choose the variable to predict",
                                        variable_names)
            
            # Display the DataFrame in the app
            st.write("Data successfully uploaded and read as DataFrame:")
            st.dataframe(df)
        except Exception as e:
            st.error(f"Error reading the file: {e}")

    if execute:
        with st.spinner("Writing code"):
            agents = AICoderAgents()
            data_define= agents.datapreprocessing(llm)
            model_assess = agents.modelbuilding(llm)
            validcode_agent = agents.validator_agent(llm)

            tasks=AICoderTasks()
            task_data_preprocess=tasks.task_data_preprocess(agent=data_define,df=df,uploaded_file=uploaded_file,predictvar=predictvar)
            task_choose_model=tasks.task_choose_model(agent=model_assess,df=df,uploaded_file=uploaded_file,predictvar=predictvar,context=[task_data_preprocess])
            task_check_code=tasks.task_check_code(agent=validcode_agent,context=[task_data_preprocess,task_choose_model])

            crew = Crew(
                agents = [data_define,model_assess,validcode_agent],
                tasks = [task_data_preprocess,task_choose_model,task_check_code],
                process = Process.sequential,
                # manager_llm=llm,
                verbose=True
            )

            results = crew.kickoff()

            st.write(results)

if __name__ == '__main__':
    main()


