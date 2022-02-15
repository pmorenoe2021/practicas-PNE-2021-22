class Seq:
    """A class for representing sequences"""
    def __init__(self):
        print("New sequence created!")


# Main program
# Create an object of the class Seq
s1 = Seq()
s2 = Seq()
print("Testing...")

###Adding data: attribute strbases
class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        print("New sequence created!")


# Main program
# Create objects of the class Seq
s1 = Seq("AGTACACTGGT")
s2 = Seq("CGTAAC")


