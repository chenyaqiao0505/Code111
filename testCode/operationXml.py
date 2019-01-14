import xml.sax


class MovieHandler(xml.sax.ContentHandler):
    def __init__(self):
       self.device = ''
       self.location = ''
        # self.CurrentData = ""
        # self.type = ""
        # self.format = ""
        # self.year = ""
        # self.rating = ""
        # self.stars = ""
        # self.description = ""

    # 元素开始事件处理
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "movie":
            title = attributes["title"]
            print("Title:", title)


    # 元素结束事件处理
    def endElement(self, tag):
        if self.CurrentData == "device":
            print("Device Number:", self.device)
        elif self.CurrentData == "location":
            print("Location:", self.location)
        self.CurrentData = ""

    # 内容事件处理
    def characters(self, content):
        if self.CurrentData == "device":
            self.device = content
        elif self.CurrentData == "location":
            self.format = content

if (__name__ == "__main__"):
    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # turn off namepsaces
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)
    parser.parse("movies.xml")