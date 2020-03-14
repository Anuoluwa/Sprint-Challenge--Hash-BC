#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    for ticket in tickets:
        # add the tickets source/destination to the hashtable as a pair
        hash_table_insert(hashtable, ticket.source, ticket.destination)

    source = ""
    position = 0

    while position < length:
        destination = hash_table_retrieve(hashtable, source)
        route[position] = destination
        source = destination
        position += 1

    return route

