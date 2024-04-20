from operations import Property

def readFile(path = "available_land"):

    file = open(path)
    dataList = {}
    for line in file:
        line_data = line.split(",")
        _kitta_number = line_data[0] #_ xa vani private variable
        _location = line_data[1]
        _direction = line_data[2]
        _anna= line_data[3]
        _price= line_data[4]
        _status = line_data[5]

        _property = Property(int(_kitta_number), _location, _direction, int(_anna), float(_price), _status.strip("\n"))

        dataList[int(_kitta_number)] = _property
        return dataList
        
