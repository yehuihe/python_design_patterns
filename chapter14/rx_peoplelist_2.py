import rx
from rx import from_, interval, operators as op


# TODO: didn't print anything yet. code from op.group_by and below is wrong.
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


def frequent_firstnames_from_db(file_name):
    file = open(file_name)

    # collect and push only the frequent firstnames
    return rx.pipe(
        op.flat_map(lambda line: from_(file)),
        op.flat_map(lambda content: content.split(', ')),
        op.filter(lambda name: name != ''),
        op.map(lambda name: name.split()[0]),
        op.group_by(lambda firstname: firstname),
        op.flat_map(lambda grp: grp.count().map(lambda ct: (grp.key, ct))),
        op.filter(lambda name_and_ct: name_and_ct[1] > 3)
    )


db_file = "people.txt"

# Emit data every 5 seconds
interval(5.0).pipe(
    frequent_firstnames_from_db(db_file)
).subscribe(lambda value: print(str(value)))

# Keep alive until user presses any key
input("Starting... Press any key to quit\n")
