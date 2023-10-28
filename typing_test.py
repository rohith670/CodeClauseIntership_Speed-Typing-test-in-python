import time

def typing_test():
    prompt_text = "The quick brown fox jumps over the lazy dog."
    print("Type the following text as fast as you can:")
    print(prompt_text)
    input("Press Enter to start the timer...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    user_input = user_input.strip()
    
    if user_input == prompt_text:
        elapsed_time = end_time - start_time
        words_per_minute = len(prompt_text.split()) / (elapsed_time / 60)
        print(f"Time: {elapsed_time:.2f} seconds")
        print(f"Words per minute: {words_per_minute:.2f}")
    else:
        print("You made a mistake. Please try again.")

if __name__ == "__main__":
    typing_test()