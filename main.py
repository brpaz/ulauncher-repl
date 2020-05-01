"""Ulauncher extension main  class"""

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

LANGUAGES = [
    {'name': 'Go', 'icon': 'images/langs/go.png', 'key': 'go'},
    {'name': 'HTML, CSS, JS', 'icon': 'images/langs/html.png', 'key': 'html'},
    {'name': 'Java', 'icon': 'images/langs/java.png', 'key': 'java'},
    {'name': 'Javascript', 'icon': 'images/langs/js.png', 'key': 'js'},
    {'name': 'NodeJS', 'icon': 'images/langs/node.png', 'key': 'nodejs'},
    {'name': 'PHP', 'icon': 'images/langs/php.png', 'key': 'php'},
    {'name': 'Python', 'icon': 'images/langs/python.png', 'key': 'python3'},
    {'name': 'Ruby', 'icon': 'images/langs/ruby.png', 'key': 'ruby'},
]


class ReplExtension(Extension):
    """ Main extension class """

    def __init__(self):
        """ init method """
        super(ReplExtension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    """ Handles Keyboard input """

    def on_event(self, event, extension):
        """ Handles the event """
        items = []

        query = event.get_argument()

        # filter and sort array of languages.
        langs = LANGUAGES
        if query:
            langs = [x for x in LANGUAGES if query.lower() in x['name'].lower()]

        items.append(ExtensionResultItem(icon='images/icon.png',
                                         name='Repl.it',
                                         description='Select to open repl.it',
                                         on_enter=OpenUrlAction('https://repl.it/')))

        for l in langs:  # pylint: disable=invalid-name
            items.append(ExtensionResultItem(icon=l['icon'],
                                             name=l['name'],
                                             description='Open Repl.it for %s language' % l['name'],
                                             on_enter=OpenUrlAction(
                                                 "https://repl.it/languages/%s" % l['key'])))

        return RenderResultListAction(items)


if __name__ == '__main__':
    ReplExtension().run()
