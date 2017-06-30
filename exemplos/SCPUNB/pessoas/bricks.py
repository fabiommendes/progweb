from bricks.helpers import safe
from bricks.html5 import div, document, title, body, meta, style
_title = title

CSS = '''
body {
    padding: 20px;
    font-size: 1.2em;
}
'''


def page(data='hello world!', title='SCPUNB'):
    return \
        document[
            meta[
                _title(title),
                style(CSS),
            ],
            body[
                div[
                    data
                ]
            ]
        ]
