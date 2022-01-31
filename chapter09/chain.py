
class Event:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Widget:

    def __init__(self, parent=None):
        self.parent = parent

    def handle(self, event):
        handler = f'handle_{event}'
        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent:
            self.parent.handle(event)
        elif hasattr(self, 'handle_default'):
            self.handle_default(event)


class MainWindow(Widget):

    @staticmethod
    def handle_close(event):
        print(f'MainWindow: {event}')

    @staticmethod
    def handle_default(event):
        print(f'MainWindow Default: {event}')


class SendDialog(Widget):

    @staticmethod
    def handle_paint(event):
        print(f'SendDialog: {event}')


class MsgText(Widget):

    @staticmethod
    def handle_down(event):
        print(f'MsgText: {event}')


def main():
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)

    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)


if __name__ == '__main__':
    main()
