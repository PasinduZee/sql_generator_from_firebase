from prettytable import PrettyTable
from utils import Utilities


class Table(object):
    def __init__(self, table_num,column_names,in_type,table_name):

        column_names.insert(0,in_type);
        column_names.insert(0, 'auto_id');
        self.table_num = table_num
        self.name = table_name
        self.column_names = column_names;
        self.data = []
        self.data_count=0;

    def insert_row(self, row,key_tail):
        self.data_count = self.data_count + 1;
        row.insert(0, key_tail);
        row.insert(0, self.data_count);
        self.data.append(row);
        return self.table_num,self.data_count;

    def get_id(self):
        return self.table_num

    def get_name(self):
        return self.name

    def get_column_names(self):
        return self.column_names

    def get_data(self):
        return self.data;

    def get_table_size(self):
        return self.data_count;

    def print_table_meta(self):
        print('Table num ='+str(self.table_num))
        print('Name ='+self.name)
        print('Size ='+str(self.data_count))
        return

    def print_table(self):

        column_count=len(self.column_names);
        self.print_table_meta();
        pretty_t = PrettyTable(self.column_names)
        for row in self.data:
            if not column_count == len(row):
                print('len(row) is not equal to len(column)');
            pretty_t.add_row(row)
        print(pretty_t);
        print();
        print();
        return


    @staticmethod
    def is_row(node):
        if isinstance(node, str):
            return False;
        is_row = True;
        for key, value in node.items():
            if isinstance(value, dict):
                is_row = False;
        return is_row

    @staticmethod
    def get_row(node):
        if not Table.is_row(node):
            print("Not a row to get values");
            return False;
        raw = [];
        for key, value in node.items():
            raw.append([key, value]);
        return raw;

    @staticmethod
    def get_columns(node):
        if not Table.is_row(node):
            print("Not a row to get values");
            return False;
        columns = [];
        for key in sorted(node.keys()):
            columns.append(key);
        return columns;

    @staticmethod
    def get_values(node):
        if isinstance(node, str):
            return node;
        if not Table.is_row(node):
            print("Not a row to get values");
            return False;
        values = [];
        for key in sorted(node.keys()):
            values.append(node[key]);
        return values;

    @staticmethod
    def get_unique_key(node):

        if isinstance(node, str):
            gen = node.split('-');
            if len(gen)>1:
                return gen[0]
            else:
                return -1;

        unique_key = "";
        for key in sorted(node.keys()):
            gen=key.split('-');
            if len(gen)>1:
                key_head, key_tail = Utilities.split_fkey(key);
                tmp_key=key_head;
            else:
                tmp_key = key;
            if unique_key != "":
                unique_key = unique_key + '__' + tmp_key;
            else:
                unique_key = tmp_key;
        return unique_key;