import random
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
ok = 0
from automaton.automaton import Automaton
from dfa.dfa import DFA

class NFA1(Automaton):

    def __init__(self, config_file):
        super().__init__(config_file)
        #print("More precisely, a NFA.")
        #print("You chose the first implementation")

    def path_creator(self):
        return super().path_creator()

    def validate_automaton(self):
        return super().validate()

    def accepts_input(self, cuvant):
        pct1 = self.begin
        for litera in cuvant:
            try:
                list_pct2 = self.paths[pct1][litera]
                pct1 = random.choice(list_pct2)
            except KeyError:
                return "donno"
            except IndexError:
                return "donno"
        if pct1 in self.finals:
            return "accept"
        else:
            return "donno"


    def read_input(self, input_str):
        return super().read_input(input_str)

class NFA2(DFA):

    def __init__(self, config_file):
        super().__init__(config_file)
        """
        print("More precisely, a NFA.")
        print("You chose the second implementation")
        """

    def path_creator(self):
        return super().path_creator()

    def validate_automaton(self):
        return super().validate()

    def transform_dfa(self):
        k = 0
        viz = []
        coada = []
        finals_aux = []
        paths_aux = {}
        coada.append(self.begin)
        while len(coada) != 0:
            #print(k)
            #print(coada, viz)
            #print(paths_aux)
            k += 1
            nod_ref = coada[0]
            viz.append(nod_ref)
            coada.pop(0)
            noduri = nod_ref.split("/--/")
            dict = {}
            for nod in noduri:
                if nod in self.finals and nod_ref not in finals_aux:
                    finals_aux.append(nod_ref)
                for cuvant in self.paths[nod]:
                    for nodb in self.paths[nod][cuvant]:
                        try:
                            if '-/'+nodb not in dict[cuvant][0]:
                                dict[cuvant][0] = dict[cuvant][0] + "/--/" + nodb
                        except KeyError:
                            dict[cuvant] = [nodb]
                    if len(self.paths[nod][cuvant])!=0:
                        dict[cuvant][0] = "/--/".join(sorted(dict[cuvant][0].split("/--/")))
                        #print(cuvant, dict[cuvant])
            for i in dict:
                if dict[i][0] not in viz and dict[i][0] not in coada and len(dict[i]) != 0:
                    coada.append(dict[i][0])
            paths_aux[nod_ref] = dict
        self.paths = paths_aux
        self.finals = finals_aux

    def validate_dfa(self):
        return super().validate_dfa()

    def accepts_input(self, cuvant):
        return super().accepts_input(cuvant)

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
    if(len(sys.argv) == 3):
        nfa = NFA2(sys.argv[1])
        nfa.read_input(nfa.config_file)
        nfa.path_creator()
        nfa.validate_automaton()
        nfa.transform_dfa()
        nfa.validate_dfa()
        print(nfa.accepts_input(sys.argv[2]))
    elif sys.argv[1] == "implementation_2":
        nfa = NFA1(sys.argv[2])
        nfa.read_input(nfa.config_file)
        nfa.path_creator()
        nfa.validate_automaton()
        print(nfa.accepts_input(sys.argv[3]))
    elif sys.argv[1] == "implementation_1":
        nfa = NFA2(sys.argv[2])
        nfa.read_input(nfa.config_file)
        nfa.path_creator()
        nfa.validate_automaton()
        #print(nfa.paths)
        nfa.transform_dfa()
        #print(nfa.paths)
        nfa.validate_dfa()
        print(nfa.accepts_input(sys.argv[3]))
    else:
        print("invalid")