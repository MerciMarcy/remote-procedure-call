class File:
  @staticmethod
  def readData(path_name):
        with open(path_name, "r") as f:
            return f.read()