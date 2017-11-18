from table import Table
from utils import Utilities
import json

Tables={};
data_tree={}
inner_id=0;
table_count=0;

middle_tree={};

def generate_data_tree(node,parent_key):
    node_items={};
    if Table.is_row(node):
        if not parent_key in data_tree:
            data_tree[parent_key] = {};
        data_tree[parent_key]=node;
        inner_id=parent_key;
    else:
        for key, value in node.items():
            if not isinstance(value,dict):
                node_items[key]=value;
            else:
                inner_id = generate_data_tree(node[key], parent_key + '__' + key);
        middle_tree[parent_key] = node_items;
    return inner_id;



def solve_leafs(data_tree_in):
    data_tree_out={};
    global table_count;
    global Tables;
    for key, value in data_tree_in.items():
        key_head,key_tail=Utilities.split_tail(key);
        unique_key=Table.get_unique_key(value);
        sql_type_row=Table.get_values(value);
        if not unique_key in Tables:
            columns=Table.get_columns(value);
            Tables[unique_key] = Table(table_count,columns,key_head,key_head);
            table_count=table_count+1;
        table_num,row_count=Tables[unique_key].insert_row(sql_type_row,key_tail);
        f_val = str(table_num) + '-' + str(row_count);
        f_key = str(table_num) + '-' + key_tail;
        if not key_head in data_tree_out:
            data_tree_out[key_head] = {};
        (data_tree_out[key_head])[f_key] = f_val;

    return data_tree_out


def solve_inner(data_tree_in):
    data_tree_out={};
    global table_count;
    global Tables;
    for key, value in data_tree_in.items():
        key_head,key_tail=Utilities.split_tail(key);
        unique_key=Table.get_unique_key(value);
        sql_type_row=Table.get_values(value);
        if not unique_key in Tables:
            columns=Table.get_columns(value);
            Tables[unique_key] = Table(table_count,columns,key_head,key_head);
            table_count=table_count+1;
        table_num,row_count=Tables[unique_key].insert_row(sql_type_row,key_tail);
        f_val=str(table_num)+'-'+str(row_count);
        f_key=str(table_num)+'-'+key_tail;

        if not key_head in data_tree_out:
            data_tree_out[key_head] = {};
        (data_tree_out[key_head])[f_key] = f_val;

        if key_head in middle_tree:
            for key, value in  middle_tree[key_head].items():
                (data_tree_out[key_head])[key] = value;
    return data_tree_out




data = json.load(open('sample2.json',encoding = "ISO-8859-1"))
generate_data_tree(data,'root');
#print(data_tree);
data_tree = solve_leafs(data_tree);
while not len(data_tree)==1:
    data_tree=solve_inner(data_tree)

for key,value in Tables.items():
    try:
        value.print_table();
    except Exception as ex:
        print(ex);
    print();

