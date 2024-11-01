# def file_exists(file_path):
#     try:
#         with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#             f.read()  # ��ȡ�ļ�������ȷ���ļ��ɶ�
#         return True
#     except FileNotFoundError:
#         return False
# # �����ļ�·��
# file_path = r"C:\Users\cnu07bj3\OneDrive - Amway Corp\Jay\teaching\Python\Python_Learning\text123.txt"
 
# # ���� file_exists ��������ļ��Ƿ����
# if file_exists(file_path):
#     print("�ļ����ڣ�")
# else:
#     print("�ļ������ڡ�")





import os
file_path = r"C:\Users\cnu07bj3\OneDrive - Amway Corp\Jay\teaching\Python\Python_Learning\text123.txt"
# ���� file_exists ��������ļ��Ƿ����
if os.path.exists(file_path):
    print("存在")
else:
    print("不存在")




def file_exists(file_path):
    return os.path.exists(file_path)

# 定义文件路径
file_path = r"C:\Users\cnu07bj3\OneDrive - Amway Corp\Jay\teaching\Python\Python_Learning\text123.txt"

# 调用 file_exists 函数检查文件是否存在
if file_exists(file_path):
    print("文件存在！")
else:
    print("文件不存在。")





def file_exists(file_path):
    return os.path.exists(file_path)
# 定义文件路径
file_path = "/path/to/file.txt"

# 调用 file_exists 函数检查文件是否存在
if file_exists(file_path):
    print("文件存在！")
else:
    print("文件不存在。")