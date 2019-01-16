def load_quotes(filename):
    with open(filename, encoding='utf8') as f:
        content = f.read()

    return list(filter(None, content.splitlines()))
