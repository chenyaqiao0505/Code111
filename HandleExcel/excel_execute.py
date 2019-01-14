from excel_gui import MyGui
from excel_method import HandleExcel
import  threading

M = MyGui()
H = HandleExcel()

def set_btu_value():
    H.allFile_url = H.get_allfile_url(H.root, H.files)
    M.btu_set = 0
    H.all_to_one(H.root, H.allFile_url, files=H.files, file_name=H.file_name, title=H.title)
    H.clear_excel(M.url_vaule, H.file_name)
    M.display_e1('数据清洗成功~！')
def set_sub_value():
    M.url_vaule = M.url_entry.get()
    H.root, H.dirs, H.files = H.get_allfile_msg(M.url_vaule)
    M.display_e1('地址导入成功~！')
    M.display_e1('当前目录路径:')
    M.display_e1(H.root)
    sum_files = len(H.get_allfile_url(H.root, H.files))
    M.display_e1('文件数量:')
    M.display_e1(sum_files)
    M.sub_btn = 0


def myhandle():
    while 1:
        if M.btu_set == 1:
            set_btu_value()
        if M.sub_btn == 1:
            set_sub_value()

t0 = threading.Thread(target=myhandle)
t0.setDaemon(1)
t0.start()

M.win.mainloop()