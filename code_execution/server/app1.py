from routes.files import predictionValue
import os,glob

def getValue():
    list_of_files = glob.glob('C:/Users/gotty/Desktop/project/myenv/server/*.weba')
    latest_file = max(list_of_files, key=os.path.getctime)
    latest_file=latest_file.replace('\\','/')
    latest_file=latest_file.replace('/','\\')
    output=predictionValue(latest_file)
    print(output)
    return output

def getValue1():
    file = "C:/Users/gotty/Desktop/project/myenv/server/Recording4.m4a"
    output = predictionValue(file)
    return output

if __name__ == "__main__":
    getValue()
