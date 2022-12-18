

def replace_by_file(old_file_path: str, match_line: str, new_line: str):
    #input file
    newText = ""
    with open(old_file_path) as f:
        newText=f.read().replace(match_line, new_line)

    with open(old_file_path, "w") as f:
        f.write(newText)        

def read_files():
    file_path = []
    return file_path

def main():
    root = "C:/Git"
    folders = ["fastapi-log"]
    file_paths = ["sample.txt", "sample2.txt", "sample3.txt"]
    
    for folder in folders:
        for file_path in file_paths:
            replace_by_file(f"{root}/{folder}/{file_path}", "ddd", "ddd-new")    

if __name__ == "__main__":
    main()