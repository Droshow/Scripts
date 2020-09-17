class Parser():
    def __init__(self):
        #[(section, option, value), (section, option, value)...]
        self.data = []
        self.sec = []
        self.paths = []

    def read(self, paths):
        self.paths = paths
        last_section = ""
        for path in paths:
            with open(path, "r") as f:
                curr_path = []
                lines = f.readlines()
                for line in lines:
                    if len(line) == 1:
                        continue
                    if line[0] == "[":
                        last_section = line[1:-2]
                        self.sec.append(line[1:-2])
                        continue
                    equals = line.find("=")
                    option = line[:equals].strip()
                    value = line[equals + 1:].strip()
                    curr_path.append([last_section, option, value])
            self.data.append(curr_path)

    def sections(self):
        return self.sec

    def set_config(self, section, option, value):
        for path in self.data:
            for d in path:
                if d[0] == section and d[1] == option:
                    if d[2][0] == '"':
                        d[2] = '"' + value + '"'
                    else:
                        d[2] = value
                    break
            else:
                continue
            break

    def write(self):
        for path in self.data:
            with open(self.paths[self.data.index(path)], "w") as f:
                section = path[0][0]
                f.write("[" + section + "]")
                for value in path:
                    if value[0] != section:
                        section = value[0]
                        f.write("\n\n[" + section + "]")
                    f.write("\n" + value[1] + " = " + value[2])



myparser = Parser()
myparser.read(["sample.cfg", "sample2.cfg"])

myparser.set_config("HKEY_LOCAL_MACHINE", "INT_TOKEN", "500")
myparser.set_config("ROAD_HOUSE", "SOME_VALUE", "BOB")

myparser.write()