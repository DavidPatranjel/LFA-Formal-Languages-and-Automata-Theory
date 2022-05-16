import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))

from dfa.dfa import DFA
# from nda.nfa import NFA

dfa = DFA('automaton.cfg')
test(dfa.accepts_string('string_1.in') == parse('string_1.out'))

nfa = NFA('automaton.cfg')
test(dfa.accepts_string('string_1.in') == parse('string_1.out'))
