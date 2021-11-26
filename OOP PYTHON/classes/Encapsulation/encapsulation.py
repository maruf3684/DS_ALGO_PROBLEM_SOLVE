
class Course(object):
    def __init__(self,course_name,language):
        self.course_name = course_name
        self.__language = language

    def set_language(self,language):
        self.__language = language

    def __get_language(self):
        return self.__language

cse=Course("Algorithm","Python")

#print (cse.__language)
print (cse.course_name)
print (cse._Course__language)

cse.set_language("Javascript")
#print (cse.get_language())
print (cse._Course__get_language())

