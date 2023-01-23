# %%
try:
    with open("test.txt", 'r') as f:
        print(f.read())
except Exception as e:
    print("File not found")
    print(e)
    print(type(e))
    with open("test.txt", "x") as f:
        f.write("Hello, I am a file")
    
# %%
