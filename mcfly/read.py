import os
import json
url = 'C:\\Users\\admin\\Desktop\\Code整理\\mcfly\\mcfly_file'


def get_allfile_msg(file_dir):
    for root, dirs, files in os.walk(file_dir):
        return root, dirs, files

files = get_allfile_msg(url)
files_name = files[2]


all_filename_list = []
for i in files_name:
    a = url +'\\'+i
    all_filename_list.append(a)


# print(all_filename_list)

# file_content = ''


# for i in all_filename_list:


files_name = []
for j in all_filename_list:
    with open(j, 'r', encoding='utf-8') as q:
        name_str = q.readline()
        # name_str1 = name_str.replace('\n','')
        # name_str2 = name_str1.replace('?', '')
        # strlist = name_str2.split('/')
        # files_name.append(strlist[len(strlist)-1])
        files_name.append(name_str)
files_name_list = []
for x in files_name:
    x.replace('?','')
    x.replace('\\n', '')
    files_name_list.append(x)
print(files_name_list)

for k,l in zip(all_filename_list,files_name_list):
    with open(j, 'r', encoding='utf-8') as w:
        if w.readline() in files_name:
            pass
        #如何使用python写文件名



# for _ in files_name:
#     for j in all_filename_list:
#         with open(j,'r')as f:
#             if _ in f.read():
#
# for m in files_name:
#     with open(m, 'w', encoding='utf-8') as f:
#         f.write()
#
#
#
#
#
# new_file_name = 'aaa'+'/'+strlist[len(strlist)-1]+'.json'
#         file_content = q.read()
#         try:
#             with open (new_file_name,'w') as l:
#                 l.write(file_content)
#         except Exception as e:
#             print(e)
