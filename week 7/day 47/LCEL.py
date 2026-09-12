from langchain_core.runnables import RunnableLambda


def uppercase(text: str) -> str:
    return text.upper()


def add_prefix(text: str) -> str:
    return f"Topic: {text}"


def add_suffix(text: str) -> str:
    return f"{text} - END"


uppercase_runnable = RunnableLambda(uppercase)
prefix_runnable = RunnableLambda(add_prefix)
suffix_runnable = RunnableLambda(add_suffix)

chain = (
    uppercase_runnable
    | prefix_runnable
    | suffix_runnable
)

result = chain.invoke("explain rag")

print(result)