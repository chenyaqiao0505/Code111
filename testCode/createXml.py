from xml.dom import minidom


# 生成XML文件方式
def generateXml():
    impl = minidom.getDOMImplementation()
    # 创建一个xml dom
    # 三个参数分别对应为 ：namespaceURI, qualifiedName, doctype
    doc = impl.createDocument(None, None, None)
    # 创建根元素
    rootElement = doc.createElement('Pythons')
    # 为根元素添加10个子元素

    deviceNum10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                   28, 29, 30, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]

    deviceLocation10 = ['162A', '167E', '16A0', '1CCE', '14E8', '170A', '1614', '14DC', '1637', '16CF',
                        '16EF', '17BA', '17CC', '14E0', '17C8', '169C', '176B', '15DB', '15DF', '175B',
                        '170C', '15C4', '15C7', '16CE', '175A', '15E3', '161B', '160F', '1713', '1644',
                        '1609', '16BF', '1736', '1758', '172C', '16CB', '15ED', '1787', '174D', '16F5', '16E5', '172B',
                        '15DC', '1742']
    for Id,Location in zip(deviceNum10,deviceLocation10):
        # 创建子元素
        childElement = doc.createElement('device')
        # 为子元素添加id属性
        childElement.setAttribute('id', str(Id))
        childElement.setAttribute('location', Location)

        # 将子元素追加到根元素中
        rootElement.appendChild(childElement)
        # print(childElement.firstChild.data)
        # 将拼接好的根元素追加到dom对象

        doc.appendChild(rootElement)

    f = open('level11.xml', 'a')
    doc.writexml(f, addindent=' ', newl='\n')
    f.close()

generateXml()