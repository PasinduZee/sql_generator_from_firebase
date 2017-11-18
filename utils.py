
class Utilities(object):

    @staticmethod
    def split_tail(key):
        key_head = "";
        gen = key.split('__');
        for i in range(0, len(gen) - 1):
            if key_head != "":
                key_head = key_head + '__' + gen[i];
            else:
                key_head = gen[i];
        key_tail = gen[len(gen) - 1];
        return key_head,key_tail;

    @staticmethod
    def split_fkey(key):
        key_head = "";
        gen = key.split('-');
        for i in range(0, len(gen) - 1):
            if key_head != "":
                key_head = key_head + '-' + gen[i];
            else:
                key_head = gen[i];
        key_tail = gen[len(gen) - 1];
        return key_head,key_tail;