from lxml import etree
import sys
import os

def get_metrics(root, test_type, val_type_len):
    test_type_node = root.find(type)
    read_node = test_type_node.find('Read')
    read_speed = read_node.text[:-val_type_len]
    write_node = test_type_node.find('Write')
    write_speed = read_node.text[:-val_type_len]
    return [read_speed, write_speed]

def parse_report(fname, reports:list):
    f = open(fname, 'r')
    f.readline()
    s = f.read()
    root = etree.fromstring(s)

    mode = root.find('.//Mode').text

    val_type_len = len(mode) + 1

    reports.append('SeqTest', )


    f.close()



for filename in os.listdir("."):



