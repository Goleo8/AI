# first line: 1
@mem.cache

def get_data(file):
    data = load_svmlight_file(file)
    return data[0],data[1]
