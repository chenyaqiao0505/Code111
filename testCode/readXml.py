from xml.dom.minidom import parse


# 获取 python节点下得所有id属性
def getTagId():
    # 获取test.xml文档对象
    doc = parse("C:\\Users\\admin\\Desktop\\Code整理\\testCode\\level2.xml")

    for node in doc.getElementsByTagName("device"):
        # 获取标签ID属性
        id_str = node.getAttribute("id")
        location_str = node.getAttribute("location")
        # 打印输出
        print(id_str,location_str)


# 获取属性ID
getTagId()