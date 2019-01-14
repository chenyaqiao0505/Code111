from tkinter import *
import tkinter.messagebox #导入tkinter模块
import xlwt
import xlrd
from tkinter import ttk


ytm=tkinter.Tk() #创建Tk对象
ytm.title("login") #设置窗口标题
ytm.geometry("900x600") #设置窗口尺寸


ss ='ACW,PASS,1.500Kv,0.019mA,T=002.0s'
num = '413213543251,'
s1 = num+ss
bookList = [(s1.split(',')),(s1.split(',')),(s1.split(',')),(s1.split(',')),(s1.split(',')),(s1.split(','))]


tree = ttk.Treeview(ytm, columns=['code', 'mode','pass','testVoltage','testCurrent','time'], show='headings')
tree.heading('code', text='条形码')
tree.heading('mode', text='工作模式')
tree.heading('pass', text='是否通过')
tree.heading('testVoltage', text='测试电压')
tree.heading('testCurrent', text='测试电流')
tree.heading('time', text='时间')

tree.column('code', width=90, anchor='center')
tree.column('mode', width=60, anchor='center')
tree.column('pass', width=60, anchor='center')
tree.column('testVoltage', width=120, anchor='center')
tree.column('testCurrent', width=100, anchor='center')
tree.column('time', width=90, anchor='center')

for item in bookList:
  tree.insert('', 'end', values=item)

tree.pack()


def exec_event():
  a = 54351354354
  return a

def event_return(event):    #触发功能,接收test传递过来的数据，然后再进行处理
  con = user_text.get()     #将结果写进treeview
  print('已触发~！',con)
  b = exec_event()
  # for i in range(10):
  tree.insert('', 9, values=[b])

  def CreateBarCode():  # 存条形码
    data = xlrd.open_workbook('BarCode.xls')
    table = data.sheets()[0]
    textcon = user_text.get()  # 获取文本框内容
    CBwrong()
    nrows = table.nrows  # 获取行数
    Result = CheckValues(0, textcon)  # 检查数据是否正确
    if Result == 1:
      user_text.delete('0', 'end')
    else:
      worksheet.write(nrows, 0, textcon)
      workbook.save('BarCode.xls')
      print(textcon, '写入成功')
      user_text.delete('0', 'end')


workbook = xlwt.Workbook(encoding='utf-8')
worksheet = workbook.add_sheet("sheets1")
TableHeads = ['条形码','工作模式','是否通过','测试电压','测试电流','时间']

col = 0
for i in TableHeads:
    worksheet.write(0,col,i)
    col+=1

workbook.save('BarCode.xls')
# tkinter.Button(ytm,text="存入结果",command=Save_16).pack() #command绑定获取文本框内容方法
textarea = tkinter.Text(ytm,height=16,width=30)
textarea.pack()




user_text=tkinter.Entry() #创建文本框
user_text.focus_set()
user_text.pack()
user_text.bind('<Key-Return>',event_return)


# user_text.bind('<Key-Return>',find_values)



ytm.mainloop() #进入主循环

