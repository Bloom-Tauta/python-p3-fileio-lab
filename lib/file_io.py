def write_file(file_name="test_file", file_content="This is a test content."):
    with open(f"{file_name}.txt", "w", encoding="utf-8") as write_file:
        return write_file.write(file_content)

def append_file(file_name="test_file", append_content="Appended content"):
    appended_file = open(f"{file_name}.txt", "a", encoding="utf-8")
    return appended_file.write(append_content)

def read_file(file_name="test_file"):
    read_file = open(f"{file_name}.txt", encoding="utf-8")
    return read_file.read()
