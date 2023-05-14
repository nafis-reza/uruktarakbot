import openai
import argparse

# Set up your OpenAI API credentials
openai.api_key = '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'

def generate_response(prompt):
    # Generate a response from the language model
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=50,
        temperature=0.8,
        n=1,
        stop=None,
        timeout=10
    )
    
    return response.choices[0].text.strip()

def chat():
    print("As salam alaikum! I am Uruk Tarak bot. How may I help you?")
    print("To exit the conversation with me type'exit'.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        prompt = f"You: {user_input}\nAI:"
        response = generate_response(prompt)
        print(response)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Chat with the GPT-3 language model in the CMD terminal.')
    parser.add_argument('--apikey', help='Your OpenAI API key')
    args = parser.parse_args()

    if args.apikey:
        openai.api_key = args.apikey

    chat()