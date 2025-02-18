"""
    creating a Bloom_filter for email application.
    it is used on the client side in browser session to determine whether the contact
    is saved or not. if yes skipped, if not it'll pop-up a window for you
    to save the new contact if you want.
"""
from bloom_filter import BloomFilter
import sqlite3

class Server:
    def __init__(self, db_path=':memory:'):
        """
        Initialize a connection to the SQLite database.
        Default is an in-memory database for testing.
        """
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._initialize_db()
    
    def _initialize_db(self):
        """Creates the contacts table if it doesn't exist."""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        ''')
        self.conn.commit()

    def load_contacts(self):
        """
        Load all contacts stored on the server.
        Returns a list of dictionaries with contact details.
        """
        self.cursor.execute("SELECT name, email FROM contacts")
        return [{'name': row[0], 'email': row[1]} for row in self.cursor.fetchall()]
    
    def search(self, contact_name):
        """
        Search for a contact by name on the server.
        Returns True if found, otherwise False.
        """
        self.cursor.execute("SELECT 1 FROM contacts WHERE name = ?", (contact_name,))
        return self.cursor.fetchone() is not None
    
    def store_contact(self, contact):
        """
        Store a new contact on the server.
        The contact should be a dictionary with 'name' and 'email' keys.
        Returns True if the contact was stored successfully, False otherwise.
        """
        try:
            self.cursor.execute("INSERT INTO contacts (name, email) VALUES (?, ?)", (contact['name'], contact['email']))
            self.conn.commit()
            return True
        except sqlite3.IntegrityError:
            return False
    
    def close(self):
        """Close the database connection."""
        self.conn.close()


class EmailApp:
    def __init__(self, server: Server, min_size):
        """
            initialize the connection to the server,
            load_contacts from the server into a bloom-filter data structure
            of size param: min_size or twice the size of the contacts
        """
        contacts_list = server.load_contacts()
        size = max(2 * abs(len(contacts_list)), min_size) # a bitarray with at least min_size bits
        self.bloom_filter = BloomFilter(size, 2) # using double_hashing with Murmur_hashing and Fowler-Noll-Vo
        for contact in contacts_list:
            self.bloom_filter.insert(contact)
        return self.bloom_filter # so here, self is the actual bloom-filter which contains the contact_list in a bitarray.


    def check_contact(self, server, contact):
        """
            Method check_contact verifies if an email is stored
            in the application.
        """
        if self.bloom_filter.contain(contact):
            return server.search(contact) # we need a double check for true. (false positive)
        else:
            return False

    
    def add_contact(self, server, contact):
        """
            Method add_contact adds a new contact to the system;
            it takes a bloom_filter and a server object, in addition
            to the new_contact to add.
            it returns true if and only if the whole process succeeds.
            in real implementations we should also synchronize the access to
            the server and Bloom filter, using a locking mechanism, and using a
            try-catch around the whole operation, rolling back (or retrying) if the call on the
            Bloom filter fails.
        """
        if server.store_contact(contact):
            self.bloom_filter.insert(contact)
            return True
        else:
            return False
        
        




