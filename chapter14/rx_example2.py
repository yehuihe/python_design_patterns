# from rx import Observable
from rx import from_, operators as op


def get_quotes():
    import contextlib, io
    zen = io.StringIO()
    with contextlib.redirect_stdout(zen):
        import this

    quotes = zen.getvalue().split('\n')[1:]
    return enumerate(quotes)


zen_quotes = get_quotes()

# can't use rx.of
# that's for arguments
# zen_quotes is an iterable. use rx.from_iterable. alias rx.from_
# https://rxpy.readthedocs.io/en/latest/reference_observable_factory.html#rx.from_iterable
from_(zen_quotes).pipe(
    op.filter(lambda q: len(q[1]) > 0)
).subscribe(lambda value: print(f"Received: {value[0]} - {value[1]}"))
