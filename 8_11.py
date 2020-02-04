mess = ['hi', "what's up", 'how you doin']
sent_messages = []

def send_messages(messages):
    while messages:
        m = messages.pop()
        sent_messages.append(m)
        print(m)

send_messages(mess[:])

print(mess)
print(sent_messages)
