import rx
from rx import from_, interval, operators as op


# TODO: didn't print anything yet. something is wrong.
def firstnames_from_db(file_name):
    file = open(file_name)

    # collect and push stored people firstnames
    return rx.pipe(
        op.flat_map(lambda line: from_(file)),
        op.flat_map(lambda content: content.split(', ')),
        op.filter(lambda name: name != ''),
        op.map(lambda name: name.split()[0]),
        op.group_by(lambda firstname: firstname),
        op.flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct))),  # ERROR here
    )


db_file = "people.txt"

# Emit data every 5 seconds
interval(5.0).pipe(
    firstnames_from_db(db_file)
).subscribe(lambda value: print(str(value)))

# Keep alive until user presses any key
input("Starting... Press any key to quit\n")
