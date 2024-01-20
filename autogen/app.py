from autogen import AssistantAgent, UserProxyAgent

config_list_mistral = [
    {
        'base_url': "http://0.0.0.0:8000",
        "model": "mistral",
        'api_key': "NULL",
    }
]
assistant = AssistantAgent(
    name="assistant", 
    llm_config={"config_list": config_list_mistral}
)

user_proxy = UserProxyAgent(
    name="user_proxy", 
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "coding", "use_docker": False},
    llm_config={"config_list": config_list_mistral},
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
        Otherwise, reply CONTINUE, or the reason why the task is not solved yet."""
)
user_proxy.initiate_chat(assistant, message="Write  python script to output number from 1 to 10")