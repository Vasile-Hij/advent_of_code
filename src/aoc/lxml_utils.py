from lxml import html
import lxml.etree
import lxml.cssselect

class HTMLHelper(object):
    @classmethod
    def parser(cls, data):
        content = data

        if isinstance(data, str):
            content = data.encode('utf-8')

        parser = html.HTMLParser()
        # return html.fromstring(content)
        # return html.fromstring(content, parser=parser)

        # parser = etree.XMLParser(
        # ns_clean=True, remove_blank_text=True, recover=True, huge_tree=True
        # )

        return lxml.etree.fromstring(content, parser=parser)

    @classmethod
    def get_data_from_html(cls, data):
        return cls.parser(data).text_content()

    @classmethod
    def get_data_from_html_selector(cls, content, selector):
        return cls.parser(content).cssselect(selector)[0].text
