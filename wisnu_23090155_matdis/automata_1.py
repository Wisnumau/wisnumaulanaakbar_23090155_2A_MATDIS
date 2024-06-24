# Anda ingin membuat sistem yang dapat mendeteksi URL mencurigakan dalam teks email. URL dianggap mencurigakan jika
# memiliki kata "login" diikuti oleh ".com" atau ".net".
# Deskripsi DFA:

# Keadaan: Q = {q0, q1, q2, q3, q4, q5}
# Alfabet input: Σ = {a-z, A-Z, ., /}
# Keadaan awal: q0
# Keadaan akhir: q5
# Fungsi transisi:
# δ(q0, 'l') = q1
# δ(q1, 'o') = q2
# δ(q2, 'g') = q3
# δ(q3, 'i') = q4
# δ(q4, 'n') = q5
# δ(q5, '.') = q6
# δ(q6, 'c') = q7
# δ(q6, 'n') = q8
# δ(q7, 'o') = q9
# δ(q9, 'm') = q10
# δ(q8, 'e') = q11
# δ(q11, 't') = q12
# Contoh:

# Input: "Please visit http://fake-login.com for more info."
# Output: True (mencurigakan)
class DFA:
    def __init__(self):
        self.states = {
            'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 
            'q7', 'q8', 'q9', 'q10', 'q11', 'q12'
        }
        self.start_state = 'q0'
        self.accept_states = {'q10', 'q12'}
        self.transitions = {
            ('q0', 'l'): 'q1',
            ('q1', 'o'): 'q2',
            ('q2', 'g'): 'q3',
            ('q3', 'i'): 'q4',
            ('q4', 'n'): 'q5',
            ('q5', '.'): 'q6',
            ('q6', 'c'): 'q7',
            ('q7', 'o'): 'q9',
            ('q9', 'm'): 'q10',
            ('q6', 'n'): 'q8',
            ('q8', 'e'): 'q11',
            ('q11', 't'): 'q12'
        }
        self.current_state = self.start_state

    def reset(self):
        self.current_state = self.start_state

    def transition(self, symbol):
        if (self.current_state, symbol) in self.transitions:
            self.current_state = self.transitions[(self.current_state, symbol)]

    def is_accepted(self, input_string):
        self.reset()
        for char in input_string:
            self.transition(char)
            if self.current_state in self.accept_states:
                return True
        return False

# Contoh penggunaan
dfa = DFA()
input_string = "Please visit http://fake-login.com for more info."
print(dfa.is_accepted(input_string))  # Output: True
