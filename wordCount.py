# coding:utf-8
# word_count.py


def word_count(source_file, word_count_file):
    """统计一个文本中词的出现次数。
    
    sourceFile为原文本，格式为“词+"\\r\\n"”，wordCountFile为统计过词频后的文本，格式为“词+"\\t"+词频+"\\r\\n"”"""
    import codecs
    word_dict = {}
    with codecs.open(source_file, "r", "utf-8") as f1:
        for line in f1:
            line = line.rstrip('\r\n')
            if line in word_dict:
                word_dict[line] += 1
            else:
                word_dict[line] = 1           
    with codecs.open(word_count_file, "w", "utf-8") as f2:
        for key, value in word_dict.items():
            f2.writelines([key, "\t", str(value), '\r\n'])

if __name__ == "__main__":            
    help(word_count)
    print("test")