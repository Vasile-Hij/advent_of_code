from lxml import html


class HTMLHelper(object):
    @classmethod
    def parser(cls, data):
        content = data

        if isinstance(data, str):
            content = data.encode('utf-8')

        parser = html.HTMLParser()

        return html.fromstring(content, parser=parser)

    @classmethod
    def get_data_from_html(cls, data):
        return cls.parser(data).text_content()
