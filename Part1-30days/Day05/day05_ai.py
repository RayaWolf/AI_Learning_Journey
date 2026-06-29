history = []
#append:add to the end
while True:
    user = input("Wolf:")
    
    if user == "exit":
        break

    history.append(
        {
            "role" : "wolf",
            "content":user
        } 
    )
    ai_reply = user
    history.append(
        {
            "role" : "AI",
            "content" : ai_reply
        }

    )
    print("AI:"+ai_reply)

print(history)

