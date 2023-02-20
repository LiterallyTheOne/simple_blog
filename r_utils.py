import docutils.core
import re


def rst_to_html(rst_text: str) -> str:
    result = docutils.core.publish_parts(source=rst_text, writer_name='html')['body']
    for i in range(5, 0, -1):
        result = result.replace(f'h{i}', f'h{i + 1}')
    # result = re.sub(r'<h(\d)>([^<]*)', r'<h\1 id="\2">\2', result)
    return result
