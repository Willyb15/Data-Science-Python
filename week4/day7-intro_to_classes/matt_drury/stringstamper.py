class StringStamper:
    """Stamps a message on the end of a string.

    $ stamper = StringStamper("Property of Matt.")
    $ stamper.stamp("Elements of Statistical Learning.")
    "Elements of Statistical Learning. Property of Matt."
    """
    def __init__(self, message):
        self.message = message

    def stamp(self, string):
        return string + " " + self.message
