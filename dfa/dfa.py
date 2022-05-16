import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from automaton.automaton import Automaton

class DFA(Automaton):

    def __init__(self, config_file):
        super().__init__(config_file)
        #print("More precisely, a DFA.")

    def path_creator(self):
        return super().path_creator()

    def validate_automaton(self):
        return super().validate()

    def validate_dfa(self):
        for pct1 in self.paths:
            for cuvant in self.paths[pct1]:
                if len(self.paths[pct1][cuvant]) > 1:
                    #print("Input is invalid - DFA")
                    exit(0)
        #return "Input is valid - DFA"

    def accepts_input(self, cuvant):
        pct1 = self.begin
        for litera in cuvant:
            try:
                pct1 = self.paths[pct1][litera][0]
            except KeyError:
                return "reject"
            except IndexError:
                return "reject"
        if pct1 in self.finals:
            return "accept"
        else:
            return "reject"

    def read_input(self, input_str):
        return super().read_input(input_str)


if __name__ == "__main__":

    num_args = len(sys.argv)
    """
    if num_args > 1:
        print(f"I see you provided {num_args-1} argument{'s' if num_args > 2 else ''} from the console.")
        print("Here's a list with all the system arguments:")
        for i, arg in enumerate(sys.argv):
            print(f"Argument {i}: {arg:>32}")
    """
    dfa = DFA(sys.argv[1])
    dfa.read_input(dfa.config_file)
    dfa.path_creator()
    dfa.validate_automaton()
    dfa.validate_dfa()
    print(dfa.accepts_input(sys.argv[2]))
