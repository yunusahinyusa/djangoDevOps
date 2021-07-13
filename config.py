from configparser import ConfigParser

def config(filename="config.ini",section = None):
    parser = ConfigParser()
    parser.read(filename)
    conn = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            conn[param[0]] = param[1]
    else :
            raise Exception('Section {0} is not found in the {1}file.'.format(section,filename))
    return conn