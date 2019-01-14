
class data:
    def __init__(self):
        self.getAllCropType = self.find_data(getAllCropType)

    def find_data(self,json_file):
        with open('api_data/%s.json'%json_file,'r') as f:
            return f