from responses import get_response
from utils import clean_input

class Chatbot:
    def __init__(self, name):
        self.name = name
        self.running = True

    def start(self):
        print(f"{self.name}: Hello! I'm here to help. Type 'exit' to end the conversation.")
        
        while self.running:
            user_input = input("You: ")
            self.handle_input(user_input)
    
    def handle_input(self, user_input):
        cleaned_input = clean_input(user_input)
        if cleaned_input == "exit":
            self.stop()
        else:
            response = get_response(cleaned_input)
            print(f"{self.name}: {response}")
    
    def stop(self):
        print(f"{self.name}: Goodbye!")
        self.running = False
