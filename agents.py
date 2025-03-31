from autogen import AssistantAgent, UserProxyAgent, GroupChat, GroupChatManager

config_list = [
    {
        "model": "llama3.2",
        "base_url": "http://localhost:11434/v1",
        "api_key": "ollama",
    }
]

llama_config = {"cache_seed": 42, "config_list": config_list}

sender = UserProxyAgent(
    name="Sender",
    system_message="Sender. Interact with analyst to discuss each email context.",
    code_execution_config=False,
)

analyst = AssistantAgent(
    name="Analyst",
    system_message="Analyst. Analyze each email context based on message from sender.",
    llm_config=llama_config,
)

evaluator = AssistantAgent(
    name="Evaluator",
    system_message="Evaluator. Agree or disagree all feedback from analyst. For your first sentence, you need to say 'Agree' or 'Disagree'. You need to explain a reason showing why you agree or disagree all feedback from analyst. For final step, you need to analyze each email context provided by sender.",
    llm_config=llama_config,
)

reporter = AssistantAgent(
    name="Reporter",
    system_message="Reporter. Report result based on feedback from evaluator. You need to report if each email is spam or not spam. You need to report these results as a table.",
    llm_config=llama_config,
)

from autogen import Agent

def custom_speaker_selection_func(last_speaker: Agent, groupchat: GroupChat):

    messages = groupchat.messages

    if last_speaker is sender:
        return analyst

    elif last_speaker is analyst:

        return evaluator

    elif last_speaker is evaluator:
        if "Agree" and not "Disagree" in messages[-1]["content"]:
            return reporter
        elif "Disagree" and not "Agree" in messages[-1]["content"]:
            return analyst
        elif "Disagree" and "Agree" in messages[-1]["content"]:
            return analyst
        elif "Agree" and "Disagree" in messages[-1]["content"]:
            return analyst
        elif not "Agree" and not "Disagree" in messages[-1]["content"]:
            return reporter

    elif last_speaker is reporter:

        return sender

def group_chat(email):
    groupchat = GroupChat(
        agents=[sender, analyst, evaluator, reporter],
        messages=[],
        max_round=12,
        speaker_selection_method=custom_speaker_selection_func,
    )
    chatmanager = GroupChatManager(groupchat=groupchat, llm_config=llama_config)
    sender.initiate_chat(
        chatmanager, message=email
    )