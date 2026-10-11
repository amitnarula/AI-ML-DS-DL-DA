def eliza_chatbot():
    print("ELIZA: Hello. I am a psychotherapist. How are you feeling today?")
    print("ELIZA: (Type 'quit' or 'exit' to end our session)")
    
    while True:
        # Get user input and convert to lowercase for easier matching
        user_input = input("\nYou: ").lower().strip()
        
        # Exit condition
        if 'quit' in user_input or 'exit' in user_input:
            print("ELIZA: Goodbye. I hope our session was helpful.")
            break
            
        # Conditional logic mimicking early pattern-matching
        elif 'i feel' in user_input:
            # Simple reflection of feelings
            feeling = user_input.split('i feel')[-1].strip()
            print(f"ELIZA: Why do you feel {feeling}?")
            
        elif 'sad' in user_input or 'unhappy' in user_input or 'stressed' in user_input:
            print("ELIZA: I am sorry to hear that you are feeling that way. Can you tell me what led to this?")
            
        elif 'family' in user_input or 'mother' in user_input or 'father' in user_input:
            print("ELIZA: Tell me more about your family relationships.")
            
        elif 'hello' in user_input or 'hi' in user_input:
            print("ELIZA: Hello there. What is on your mind today?")
            
        else:
            # Default canned response when no specific pattern matches
            print("ELIZA: Please go on. Tell me more about that.")

if __name__ == "__main__":
    eliza_chatbot()