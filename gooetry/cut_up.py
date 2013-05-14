from sys import argv

file_one = argv[1]
file_two = argv[2]

 
def import_text(_file):
    #Clean up text files for merge
    f = open(_file, 'r')
    text = [word for word in f.readlines()]
    text = [word.strip('\n') for word in text]
    f.close()
    return text


def combine_text(text_one, text_two):
    #Merge the two text files into a tuple
    zipped_tuple = zip(text_one, text_two)
    merged_list = list(zipped_tuple)
    # print merged_list
    for i in range(len(merged_list)):
        text = [str(item) for item in merged_list[i]]
        strings = ' '.join(text)
        print strings


text_one = import_text(file_one)
text_two = import_text(file_two)
combine_text(text_one, text_two)