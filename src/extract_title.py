def extract_title(markdown):
    lines = markdown.split("\n")
    lines = [line.strip() for line in lines]
    for line in lines:
        if line[:2] == "# ":
            return line[2:]
    raise Exception ("No header found.")