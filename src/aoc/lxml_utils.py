from lxml import html


class HTMLHelper(object):
    @staticmethod
    def content_helper(data):
        content = data
        
        if isinstance(data, str):
            content = data.encode('utf-8')     
            
        parser = html.HTMLParser()
        
        return html.fromstring(content, parser=parser)
