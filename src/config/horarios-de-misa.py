try:
    with open('../data/horarios-de-misa.md', 'r', newline='') as file:
        text = file.read()
        content=text.replace("\n","\\n")
        print(content)
except FileNotFoundError:
    print("Error: The file was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

if content != '':
    mensaje={}
    mensaje['horarios']=content