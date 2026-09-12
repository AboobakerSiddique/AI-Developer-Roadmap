from langchain_core.runnables import RunnableLambda
uppercase = RunnableLambda(lambda x: x.upper())

result1 = uppercase.invoke(" hello world ")

suffix = RunnableLambda(lambda x: x + "as a programmer")
result2 = suffix.invoke(result1)

prefix = RunnableLambda(lambda x: "Explain" + x )
result3 = prefix.invoke(result2)

print(result3)