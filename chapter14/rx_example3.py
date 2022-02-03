import rx
from rx import from_, interval, operators as op


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

# implementation 1st: inline "Observable pipeline" of operations
# interval(5.0).pipe(
#     op.flat_map(lambda seq: from_(zen_quotes)),
#     op.flat_map(lambda q: from_(q[1].split())),
#     op.filter(lambda s: len(s) > 2),
#     op.map(lambda s: s.replace('.', '').replace(',', '').replace('!', '').replace('-', '')),
#     op.map(lambda s: s.lower())
# ).subscribe(lambda value: print(f"Received: {value}"))


# implementation 2nd: operator is implemented as a composition of other operators
def custom_operator():
    return rx.pipe(
        op.flat_map(lambda seq: from_(zen_quotes)),
        op.flat_map(lambda q: from_(q[1].split())),
        op.filter(lambda s: len(s) > 2),
        op.map(lambda s: s.replace('.', '').replace(',', '').replace('!', '').replace('-', '')),
        op.map(lambda s: s.lower()),
    )


interval(5.0).pipe(
    custom_operator()
).subscribe(lambda value: print(f"Received: {value}"))


input("Starting... Press any key to quit\n")
