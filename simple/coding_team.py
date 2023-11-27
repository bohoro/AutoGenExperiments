import autogen

config_list_gpt4 = autogen.config_list_from_json(
    "OAI_CONFIG_LIST",
    filter_dict={
        "model": ["gpt-4", "gpt-4-0314", "gpt4", "gpt-4-32k", "gpt-4-32k-0314", "gpt-4-32k-v0314"],
    },
)

llm_config = {"config_list": config_list_gpt4}
user_proxy = autogen.UserProxyAgent(
   name="User_proxy",
   code_execution_config={"use_docker": False, "last_n_messages": 3, "work_dir": "groupchat"},
   # system_message="You can provide feedback on the technical solution.",
   human_input_mode="ALWAYS"
)

swe = autogen.AssistantAgent(
    name="SoftwareEngineer",
    # system_message="Your role as a SoftwareEngineer is to provide a coded technical solution in Python. You take feedback from the critic and the user proxy and improve the solution accordingly.",
    llm_config=llm_config,
)
critic = autogen.AssistantAgent(
    name="Critic",
    system_message="As the critic you do your best to improve the techncial solution. Including but not limited to feedback on code quality, readability, efficiency, and execution output. Your feedback should be constructive and actionable.",
    llm_config=llm_config,
)

groupchat = autogen.GroupChat(agents=[user_proxy, swe, critic], messages=[], max_round=15)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)

user_proxy.initiate_chat(manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software.")

# type exit to terminate the chat
