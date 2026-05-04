def load_prompt(filename):
    with open(f"prompts/{filename}", "r") as file:
        return file.read()