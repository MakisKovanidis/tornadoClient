import globalSettings
from Client import Client

def getAllConecctedSensors():
    path = globalSettings.laptopBaseDir
    pathData = globalSettings.laptopDataDir
    dirs = os.listdir(path)
    counter = 1



if __name__ == "__main__":
    client = Client("ws://localhost:3000", 5)