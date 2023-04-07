import os

__version_info__ = (0, 1, 0)
__version__ = '.'.join(map(str, __version_info__))

def get_path():
    """
    Shortcut for users whose theme is next to their conf.py.
    """
    # Theme directory is defined as our parent directory
    return os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


def update_context(app, pagename, templatename, context, doctree):
    context['theme_version'] = __version__


def setup(app):

    app.add_html_theme('name_of_theme', os.path.abspath(os.path.dirname(__file__)))

    app.connect('html-page-context', update_context)
    return {'version': __version__, 'parallel_read_safe': True}
