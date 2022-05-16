sigma, states, transitions = [], [], []
class Automaton():
    paths = {}
    begin, finals = 0, []
    def __init__(self, config_file):
        self.config_file = config_file
        #print("Hi, I'm an automaton!")

    def path_creator(self):
        for state in states:
            aux = {}
            for cuvant in sigma:
                aux[cuvant] = []
            self.paths[state] = aux
        for tranzitie in transitions:
            self.paths[tranzitie[0]][tranzitie[1]].append(tranzitie[2])

    def validate(self):
        """Return a Boolean

        Returns true if the config file is valid,
        and raises a ValidationException if the config is invalid.
        """
        for transition in transitions:
            if (transition[0] not in states) or (transition[1] not in sigma) or (transition[2] not in states):
                print("invalid")
                exit(0)
        #print("Input is valid - AUTOMATON")


    def accepts_input(self, input_str):
        """Return a Boolean

        Returns True if the input is accepted,
        and it returns False if the input is rejected.
        """
        pass

    def read_input(self, input_str):
        """Return the automaton's final configuration
        
        If the input is rejected, the method raises a
        RejectionException.
        """
        f = open(input_str)
        def readSigma(line):
            line = f.readline().strip()
            while not line == "End":
                sigma.append(line)
                line = f.readline().strip()

        def readStates(line):
            start = 0
            line = f.readline().strip().replace(",", "")
            while not line == "End":
                aux = line.split()
                if (len(aux) > 1):
                    if 'S' in aux:
                        start = start + 1
                        self.begin = aux[0]
                    if 'F' in aux:
                        self.finals.append(aux[0])
                states.append(aux[0])
                line = f.readline().strip().replace(",", "")
            if start != 1:
                print("invalid")
                exit(0)

        def readTransitions(line):
            line = f.readline().strip().replace(",", "")
            while not line == "End":
                aux = line.split()
                aux2 = (aux[0], aux[1], aux[2])
                if(tuple(aux2) not in transitions):
                    transitions.append(tuple(aux2))
                line = f.readline().strip().replace(",", "")

        for i in range(3):
            line = f.readline()
            while line.startswith("#"):
                line = f.readline()
            line = line.strip()
            if line == "Sigma :":
                readSigma(line)
            elif line == "States :":
                readStates(line)
            elif line == "Transitions :":
                readTransitions(line)

        #print("Input was read")
        pass
    

if __name__ == "__main__":
    a = Automaton('date.in')
    a.read_input("date.in")
    a.path_creator()
    print(a.paths)
    print(a.begin)
    print(a.validate())