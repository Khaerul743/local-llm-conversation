from src.services.chat_service import ChatService

chat_service = ChatService()

conversation_id = chat_service.create_conversation()

# chat_service.send_message(conversation_id, "Apa itu filsafat berdasarkan document")

# history = chat_service.get_history(conversation_id)
# print(history)

for chunk in chat_service.stream_message(
    conversation_id, "apa itu filsafat berdasarkan document"
):
    print(chunk, end="", flush=True)
