def handleChatUploadedFile(file):
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]
    

    