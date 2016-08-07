#!/usr/bin/env python
"""
__author__: super
blog : http://blog.csdn.net/songfreeman
this program return  a float value. run in 3.x
"""
import re


# ��ʽ���ַ���
def format_string(string):
    string = string.replace("--", "+")
    string = string.replace("-+", "-")
    string = string.replace("++", "+")
    string = string.replace("+-", "-")
    string = string.replace("*+", "*")
    string = string.replace("/+", "/")
    string = string.replace(' ', '')
    return string


# �����ʽ�Ϸ���
def check_expression(string):
    check_result = True
    # �����Ƿ�ƥ��
    if not string.count("(") == string.count(")"):
        print("���ʽ����,����δ�պ�!")
        check_result = False
    if re.findall('[a-z]+', string.lower()):
        print("���ʽ����,�����Ƿ��ַ�!")
        check_result = False


    return check_result


# ����� ������#(30+6*2)
def calc_mul_div(string):
    # ���ַ����л�ȡһ���˷�������ı��ʽ
    #regular = "\d+\.{0,}\d{0,}[\*\/][\-]{0,}\d+\.{0,}\d{0,}"
    regular='\d+\.?\d*([*/]|\*\*)[\-]?\d+\.?\d*'
    # ��������ҵ��˻�������ʽ
    while re.findall(regular, string):
        # ��ȡ���ʽ
        expression = re.search(regular, string).group()

        # ����ǳ˷�
        if expression.count("*")==1:
            # ��ȡҪ�����������
            x, y = expression.split("*")
            # ������
            mul_result = str(float(x) * float(y))
            # ������ı��ʽ�滻Ϊ������ֵ
            string = string.replace(expression, mul_result)
            # ��ʽ��һ��
            string = format_string(string)

        # ����ǳ���
        if expression.count("/"):
            # ��ȡҪ�����������
            x, y = expression.split("/")
            # �������
            div_result = str(float(x) / float(y))
            # �ý���滻���ʽ
            string = string.replace(expression, div_result)
            string = format_string(string)

        if expression.count('*')==2:
            x,y=expression.split('**')
            pow_result=1
            for i in range(int(y)):
                pow_result*=int(x)
            string=string.replace(expression,str(pow_result))
            string=format_string(string)
    return string


# ����ӡ�����
def calc_add_sub(string):
    #(30+12-23+24-3)
    # ����������ʽ
    # add_regular = "[\-]{0,}\d+\.{0,}\d{0,}\+[\-]{0,}\d+\.{0,}\d{0,}"
    # sub_regular = "[\-]{0,}\d+\.{0,}\d{0,}\-[\-]{0,}\d+\.{0,}\d{0,}"
    add_regular='[\-]?\d+\.?\d*\+[\-]?\d+\.?\d*'
    sub_regular='[\-]?\d+\.?\d*\-[\-]?\d+\.?\d*'

    # ��ʼ�ӷ�
    while re.findall(add_regular, string):
        # �����еļӷ�������,��ȡ���мӷ����ʽ
        add_list = re.findall(add_regular, string)
        for add_str in add_list:
            # ��ȡ�����ӷ�����
            x, y = add_str.split("+")
            add_result = "+" + str(float(x) + float(y))
            string = string.replace(add_str, add_result)
        string = format_string(string)

    # ��ʼ����
    while re.findall(sub_regular, string):
        sub_list = re.findall(sub_regular, string)
        for sub_str in sub_list:
            numbers = sub_str.split("-")
            # -3-5�����split�᷵��3��ֵ
            if len(numbers) == 3:
                result = 0
                for v in numbers:
                    if v:
                        result -= float(v)
            else:
                x, y = numbers
                result = float(x) - float(y)
            # �滻�ַ���
            string = string.replace(sub_str, "+" + str(result))
        string = format_string(string)
    return string


if __name__ == "__main__":

    #source = "1 - 2 *  ( (60-30 +(-9-2-5-2*3-5/3-40*4/2-3/5+6*3) * (-9-2-5-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    #source = "2-     ((-40/5)*(4-3))"
    #source="3**2"
    source="3*6*8"

    if check_expression(source):
        print("source: ", source)
        print("eval result: ", eval(source))
        source = format_string(source)
        print(source)

        while source.count("(") > 0:
            # ��ʽ��
            # ȥ����,�õ����ŵ��ַ���,�����:(30+6/3)
            strs = re.search('\([^()]*\)', source).group()
            # �����ŵı��ʽ���гˡ�������
            replace_str = calc_mul_div(strs)
            # ������Ľ���ڽ��мӡ�������
            replace_str = calc_add_sub(replace_str)
            # �����ŵ��ַ����滻Ϊ������,�������(),�滻ʱȥ��():[1:-1]
            source = format_string(source.replace(strs, replace_str[1:-1]))

        else:
            # û�����ž͵����һ���ʽ��
            replace_str = calc_mul_div(source)
            # ��˳�
            replace_str = calc_add_sub(replace_str)
            # ��Ӽ�
            source = source.replace(source, replace_str)
        print("my result: ", source.replace("+", ""))