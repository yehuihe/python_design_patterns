# from rx import Observable, Observer
from rx import create


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return quotes


def push_quotes(observer, scheduler):

    quotes = get_quotes()
    for q in quotes:
        if q:  # skip empty
            observer.on_next(q)
    observer.on_completed()


# ERROR in original Kamon's repository. RxPy 3.2.0 compatibility issue
# RxPy 3.2.0 made changes that cancelled Observer class

# class ZenQuotesObserver(Observer):
#
#     def on_next(self, value):
#         print(f"Received: {value}")
#
#     def on_completed(self):
#         print("Done!")
#
#     def on_error(self, error):
#         print(f"Error Occurred: {error}")


source = create(push_quotes)

# source.subscribe(ZenQuotesObserver())
source.subscribe(
    on_next=lambda i: print("Received {0}".format(i)),
    on_error=lambda e: print("Error Occurred: {0}".format(e)),
    on_completed=lambda: print("Done!"),
)
