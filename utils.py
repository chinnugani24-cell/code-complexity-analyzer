def clean_code(code):
    # Remove empty lines and strip spaces
    lines = code.split("\n")
    cleaned = [line.strip() for line in lines if line.strip() != ""]
    return "\n".join(cleaned)