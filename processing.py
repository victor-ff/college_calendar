import pandas

def ReadFile():
    return pandas.read_json("calendar.json")

def SchoolSubjects(dataframe):
    for index in dataframe.keys():
        if index == "MATERIAS":
            return dataframe[index].keys()

def InformationOfSubjetcs(dataframe):
    index = "MATERIAS"
    for subjetc in dataframe[index].keys():
        information = dataframe[index][subjetc]
        print("Materia: {}".format(subjetc))        # Print no terminal "Materia: {}"
        for info in information.keys():
            print(info, ":", information[info])




dataframe = ReadFile()

