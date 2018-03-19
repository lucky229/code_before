'''
html——output.py上面爬虫流程图中的【应用器】
负责对解析后的数据应用，这里简单用一个WEB页面把爬取的所有存在datas列表的数据以table输出
'''
import time

class HtmlOutput(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        filename = time.strftime("%Y-%m-%d_%H-%M-%S")
        with open("out_%s.html" % filename, "w", encoding='utf-8') as f_out:
            f_out.write("<html>")
            f_out.write(r'<head>'
                        r'<link rel="stylesheet"'
                        r'crossorigin="anonymous"></head>')
            f_out.write("</body>")
            f_out.write(r'<table class="table table_bordered table-hover">')

            item_css = ['active', 'sucess', 'warning', 'info']
            for data in self.datas:
                index = self.datas.index(data) % len(item_css)
                f_out.write(r'<tr class="'+item_css[index]+r'">')
                f_out.write('<td>%s<td>' % data["url"])
                f_out.write('<td>%s<td>' % data["title"])
                f_out.write('<td>%s<td>' % data["summary"])
                f_out.write('</tr>')

            f_out.write("</table>")
            f_out.write("</body>")
            f_out.write("</html>")
