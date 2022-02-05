import sys
import sqlite3
import csv

cache_key_prefix = "quote"


class QuoteCache:

    def __init__(self, filename=""):
        self.filename =  filename

    def get(self, key):
        with open(self.filename) as csv_file:
            items = csv.reader(csv_file, delimiter=';')
            for item in items:
                if item[0] == key.split('.')[1]:
                    return item[1]

    def set(self, key, quote):
        existing = []
        with open(self.filename) as csv_file:
            items = csv.reader(csv_file, delimiter=';')
            existing = [cache_key_prefix + "." + item[0] for item in items]

        if key in existing:
            print("This is weird. The key already exists.")
        else:
            # save the new data
            with open(self.filename, "a", newline="") as csv_file:
                writer = csv.DictWriter(csv_file,
                                        fieldnames=['id', 'text'],
                                        delimiter=";")
                # print(f"Adding '{q[1]}' to cache")
                writer.writerow({'id': key.split('.')[1], 'text': quote})

    def delete(self, key):
        existing = []
        with open(self.filename) as csv_file:
            items = csv.reader(csv_file, delimiter=';')
            existing = [cache_key_prefix + "." + item[0] for item in items]

        if key in existing:
            # delete the row with key
            quotes = []
            with open(self.filename) as csv_file:
                items = csv.reader(csv_file, delimiter=';')
                for item in items:
                    cache_key = cache_key_prefix + "." + item[0]
                    if key != cache_key:
                        quote_id = item[0]; quote_text = item[1]
                        quote = (quote_id, quote_text)
                        quotes.append(quote)

            # Populate the cache with quotes
            with open(self.filename, "w", newline="") as csv_file:
                writer = csv.DictWriter(csv_file,
                                        fieldnames=['id', 'text'],
                                        delimiter=";")
                for q in quotes:
                    writer.writerow({'id': str(q[0]), 'text': q[1]})
        else:
            print("This is weird. The key does not exist.")


cache = QuoteCache('data/quotes_cache.csv')


def get_quote(quote_id):
    # Return the item from cache if found in it. If not found in cache, read from data store.
    # Put the read item in cache and return it.

    quote = cache.get(f"quote.{quote_id}")
    out = ""

    if quote is None:
        try:
            db = sqlite3.connect('data/quotes.sqlite3')
            cursor = db.cursor()
            cursor.execute(f"SELECT text FROM quotes WHERE id = {quote_id}")
            for row in cursor:
                quote = row[0]
            print(f"Got '{quote}' FROM DB")
        except Exception as e:
            print(e)
        finally:
            # Close the db connection
            db.close()

        # ORIGINAL ERROR: cache will still add empty quote with quote_id if quote is not in db
        # only when quote exists in db then it will add to the cache
        if quote:
            # and add it to the cache
            key = f"{cache_key_prefix}.{quote_id}"
            cache.set(key, quote)

    if quote:
        out = f"{quote} (FROM CACHE, with key 'quote.{quote_id}')"

    return out


def update_quote(quote_id, quote_text):
    # The update part of the cache-aside implementation
    # write the item in the database and remove the corresponding entry from cache

    quote = cache.get(f"quote.{quote_id}")
    out = ""

    try:
        db = sqlite3.connect('data/quotes.sqlite3')
        cursor = db.cursor()
        cursor.execute(f"SELECT text FROM quotes WHERE id = {quote_id}")
        exist = False
        for row in cursor:
            if row:
                exist = True
        if exist:
            cursor.execute(f'''
                UPDATE quotes SET text = ? WHERE id = ?
            ''', (quote_text, quote_id))
            out = f"'UPDATED to {quote_text}', with key ''quote.{quote_id}''"
        else:
            print("This is weird. The key does not exist.")
    except Exception as e:
        print(e)
    finally:
        # Save (commit) the changes
        db.commit()
        # Close the db connection
        db.close()

    if quote:
        # remove the corresponding entry from cache
        key = f"{cache_key_prefix}.{quote_id}"
        cache.delete(key)
        print(f"Deleted {quote} (FROM CACHE, with key 'quote.{quote_id}')")

    return out


if __name__ == '__main__':
    args = sys.argv

    if args[1] == 'fetch':
        while True:
            quote_id = input('Enter the ID of the quote: ')
            q = get_quote(quote_id)
            if q:
                print(q)

    elif args[1] == 'update':
        from faker import Faker

        fake = Faker()
        while True:
            quote_id = input('Enter the ID of the quote you want to update: ')
            q = update_quote(quote_id, fake.sentence())
            if q:
                print(q)
