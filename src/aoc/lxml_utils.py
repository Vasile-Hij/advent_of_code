from lxml import html


def content_helper(data):
    content = data
    
    if isinstance(data, str):
        content = data.encode('utf-8')     
        
    parser = html.HTMLParser()
    
    return html.fromstring(content, parser=parser)
 
 
def lxml_select(content):
    return content.text_content()

