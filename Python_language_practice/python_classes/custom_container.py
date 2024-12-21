# __ is for private variable declaration like __variable
class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, item):
        return self.__tags.get(item.lower(), 0)

    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud()
cloud["python"] = 10
cloud["anaconda"] = 2
print(len(cloud))
cloud.add("python")
cloud.add("Python")
# print(cloud.tags)
print(cloud.__dict__)
"""print(cloud._TagCloud__tags) 
# according to the above line we can conclude that python does not have private members 
# like other languages and is still accessible from outside"""
