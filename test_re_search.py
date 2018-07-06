import re


# re.search方法是什么?
def test_what_is_re_search():
    str1 = r"hello. hello. world "
    regex = r"hello"
    result = re.search(regex, str1)
    print(type(result))
    print(result)
    print(result.group())

    '''
    output:
        <class '_sre.SRE_Match'>
        <_sre.SRE_Match object; span=(0, 5), match='hello'>
        hello
    说明:
    对search的解释是:
         search是对match的 推广吧,放松了条件,  检查str1里面是否包含regex. 所以从这个角度说, search和findall方法很相似.
         search发现又一次匹配, 就会结束查找.  
    search应用场景:
       暂时不清楚. 
    '''


if __name__ == '__main__':
    test_what_is_re_search()