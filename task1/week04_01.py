import os.path
import tempfile


class File:

    @staticmethod
    def read_by_name(file_name):
        with open(file_name, "r") as f:
            return f.read()

    def read(self):
        return self.read_by_name(self.file_name)

    def write(self, data):
        with open(self.file_name, "w") as f:
            f.write(data)

    def __str__(self):
        return os.path.abspath(self.file_name)

    def __init__(self, file_name):
        self.file_name = file_name
        if not os.path.exists(file_name):
            with open(self.file_name, 'a'):
                pass

    def __getitem__(self, index):
        with open(self.file_name, 'r') as f:
            self.content = f.readlines()
        if len(self.content) > 0 and index < len(self.content):
            return self.content[index]
        else:
            raise StopIteration

    def __add__(self, other):
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        res_file = File(temp_file.name)
        res_file.write(self.read() + self.read_by_name(other.file_name))
        return res_file

# path_to_file = 'some_filename'
# print(os.path.exists(path_to_file))
#
# file_obj = File(path_to_file)
# print(os.path.exists(path_to_file))
#
# print(file_obj.read())
#
# file_obj.write('some text')
#
# print(file_obj.read())
#
# file_obj.write('other text')
#
# print(file_obj.read())
#
# print(file_obj)
#
# file_obj_1 = File(path_to_file + '_1')
# file_obj_2 = File(path_to_file + '_2')
# file_obj_1.write('line 1\n')
# file_obj_2.write('line 2\n')
#
# new_file_obj = file_obj_1 + file_obj_2
# print(isinstance(new_file_obj, File))
# print(new_file_obj)
# print(new_file_obj.read())
#
# for line in new_file_obj:
#     print(ascii(line))