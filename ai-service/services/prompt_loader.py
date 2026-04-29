def load_prompt():
    with open("prompts/vendor_prompt.txt", "r") as file:
        return file.read()