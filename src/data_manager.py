import json

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def save_data(self, data):
        with open(self.file_path, 'w') as file:
            json.dump(data, file)

    def load_data(self):
        with open(self.file_path, 'r') as file:
            return json.load(file)
