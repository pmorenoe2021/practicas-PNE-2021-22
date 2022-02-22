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
        return len(self.strbases)

    def count_base(self):
        let_a = 0
        let_c = 0
        let_g = 0
        let_t = 0
        for l in self:
            if l.upper() == "A":
                let_a += 1
            elif l.upper() == "C":
                let_c += 1
            elif l.upper() == "G":
                let_g += 1
            elif l.upper() == "T":
                let_t += 1
        return let_a, let_c, let_g, let_t
