class Seq:
    """A class for representing sequences"""

    def __init__(self, strbases ="NULL"):
        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases
        if self.strbases == "NULL":
            print("NULL se created")

        elif not self.valid_seq():
            self.strbases = "ERROR"
            print("INVALID Seq!")

        else:
            print("New sequence created!")


    # this makes sequence become a normal argument
    @staticmethod
    def valid_seq2(sequence):
        valid = True
        i = 0
        while i < len(sequence) and valid:
            c = sequence[i]
            if c != "A" and c != "C" and c != "T" and c != "G":
                valid = False
            i += 1
        return valid


    def valid_seq(self):
        valid = True
        i = 0
        while i < len(self.strbases):
            c = self.strbases[i]
            if c != "A" and c != "C" and c != "T" and c != "G":
                valid = False
            i += 1
        return valid


    def __str__(self):
        """Method called when the object is being printed"""

        # -- We just return the string with the sequence
        return self.strbases

    def len(self):
        """Calculate the length of the sequence"""
        result = 0
        if self.strbases == "ERROR" or self.strbases == "NULL":
            result = 0
        else:
            result = len(self.strbases)
        return result

    def count_base(self, list_bases):
        count = 0
        if self.strbases == "ERROR" or self.strbases == "NULL":
            count = 0
        else:
            for s in self.strbases:
                if s == list_bases:
                    count += 1
        return count

