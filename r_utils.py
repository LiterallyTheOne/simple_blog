import docutils.core
import re


def rst_to_html(rst_text: str) -> str:
    # TODO I need to make it more general
    result = docutils.core.publish_parts(
        source=rst_text, writer_name='html')['body']
    # make headers smaller to have the main header in h1
    for i in range(5, 0, -1):
        result = result.replace(f'h{i}', f'h{i + 1}')
    # change cite to code to have the style that I want
    result = result.replace('<cite>', '<code class="rounded p-1">')
    result = result.replace('</cite>', '</code>')
    # change pre to
    result = re.sub(r'<pre class="literal-block">((.|\s)*?)(?=<\/pre>)',
                    r'<pre><code>\1</code></pre>', result)
    result = re.sub(r'<pre class="code literal-block">((.|\s)*?)(?=<\/pre>)',
                    r'<pre><code>\1</code></pre>', result)

    # A naive solution to fix the path problems
    result = result.replace('src="media', 'src="/media')

    return result
