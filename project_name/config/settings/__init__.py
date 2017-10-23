# import sqlite3
#
#
# class Model(object):
#     def __init__(self, db, table):
#         """
#             :param db: name database
#             :param table: name table
#             :return: return object table
#         """
#         self.db = db
#         self.table = table
#         self.connection = sqlite3.connect(db + '.db')
#         self.connection.row_factory = sqlite3.Row
#
#     def create(self, row):
#         """
#              :param row: dict()
#         """
#         bindings = '('
#         keys = '('
#         values = list()
#         i = 0
#         for key, value in row.items():
#             bindings += '?'
#             keys += key
#             values.append(value)
#             i += 1
#             if i != (len(row)):
#                 bindings += ', '
#                 keys += ', '
#         bindings += ')'
#         keys += ')'
#         sql = f'INSERT INTO {self.table} {keys} VALUES {bindings}'
#         self.connection.execute(sql, values)
#         self.connection.commit()
#
#     def read(self):
#         sql = 'SELECT * FROM {}'.format(self.table)
#         cursor = self.connection.execute(sql)
#         rows = list()
#         for row in cursor:
#             rows.append(row)
#         return rows
#     def read(self):
#         sql = 'SELECT * FROM {}'.format(self.table)
#         cursor = self.connection.execute(sql)
#         rows = list()
#         for row in cursor:
#             rows.append(row)
#         return rows
#
#     def update(self, row, where):
#         """
#             :param row: dict()
#             :param where: dict()
#         """
#         keys = ''
#         values = list()
#         i = 0
#         for key, value in row.items():
#             keys += key + ' = ?'
#             values.append(value)
#             i += 1
#             if i != len(row):
#                 keys += ', '
#         sql = f'UPDATE {self.table} SET {keys} WHERE {where["key"]} = {where["value"]}'
#         self.connection.execute(sql, values)
#         self.connection.commit()
#
#     def delete(self, where):
#         """
#             :param where: dict()
#         """
#         key = where['key']
#         value = where['value']
#         sql = f'DELETE FROM {self.table} WHERE {key} = {value}'
#         self.connection.execute(sql)
#         self.connection.commit()
#
#     @staticmethod
#     def toCSV(data, fname="output.csv"):
#         with open(fname, 'a') as file:
#             file.write(",".join([str(j) for i in data for j in i]))
#
#
# def main():
#     pass
#     # m = Model('test', 'test')
#     # m.create(dict(t1='dudez', i1=9876))
#     # m.update(dict(t1='faz', i1=2345), dict(key='i1', value=1234))
#     # m.delete(dict(key='i1', value=4))
#     # print(m.read())
#
# if __name__ == "__main__":
#     main()
