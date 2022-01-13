class FileManager:
    def __init__(self,file_name):
        self.file_name=file_name

    def read_file(text_data):
        f = open(text_data, 'r')
        fc = f.read()
        print(fc)
        f.close()

    def update_file(text_data):
        f = open(text_data, "a")
        f.write("Patryk, Eryk")
        f.close()