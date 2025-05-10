from transformers import pipeline

# Initialize the text generator
text_generator = pipeline("text-generation", model="gpt2")  # Fast and lightweight

def complete_text(prompt):
    # Generate text completion
    output = text_generator(
        prompt,
        max_length=50,          # Adjust length as needed
        num_return_sequences=1, # Number of completions
        truncation=True
    )
    return output[0]['generated_text']

# Example usage
if __name__ == "__main__":
    user_input = input("Enter your starting text: ")
    completed_text = complete_text(user_input)
    print("\nCompleted Text:")
    print(completed_text)