class FA:
    def __init__(self, states, transitions, start_state, accept_states):
        self.states = states
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states
        
    def recognize(self, string):
        current_state=self.start_state
        for char in string:
            if char in self.transitions[current_state]:
                current_state=self.transitions[current_state][char]
            else:
                return False
        return current_state in self.accept_states

def main():
	#An FA (M1) which recognizes the set of strings over {0,1} that ends with 0.
	#Setting M1 states transistions, start_state, accept_state
	M1_states = {"s0","s1","s2"}
	M1_transitions = {
		"s0":{'0':"s1", '1':"s2"},
		"s1":{'0':"s1", '1':"s2"},
		"s2":{'0':"s1", '1':"s2"}
	}
	M1_start_state = "s0"
	M1_accept_states = {"s1"}
	M1_fa = FA(M1_states, M1_transitions, M1_start_state, M1_accept_states)
	M1_strings = ["Ʌ", "100", "011", "10abc1", "0", "1", "0101011", "11010", "0001", "1110"]


	#An FA (M2) which recognizes the set of strings over {0,1} that do not have two consecutive 1's.
	#Setting M2 states transistions, start_state, accept_state
	M2_states = {"s0","s1","s2","s3","s4"}
	M2_transitions = {
		"s0": {'0': "s0", '1': "s1"},
		"s1": {'0': "s0", '1': "s2"},
		"s2": {'1': "s2", '0':"s2"}
	}
	M2_start_state = "s0"
	M2_accept_states = {"s0", "s1"}
	M2_fa = FA(M2_states, M2_transitions, M2_start_state, M2_accept_states)
	M2_strings = ["Ʌ", "1", "000", "101", "111", "01001", "1011011", "1011000", "01010", "1010101110"]


	#An FA (M3) which recognizes all identifiers that begin with a letter (both upper and lower) and followed by
	#any number of letters and digits.
	#Setting M3 states transistions, start_state, accept_state
	M3_states = {"s0", "s1","s2"}
	M3_transitions = {
	"s0": {'a': "s1",'b': "s1",'c': "s1",'d': "s1",'e': "s1",'f': "s1",'g': "s1",'h': "s1",'i': "s1",'j': "s1",'k': "s1",'l': "s1",
			'm': "s1",'n': "s1",'o': "s1",'p': "s1",'q': "s1",'r': "s1",'s': "s1",'t': "s1",'u': "s1",'v': "s1",'w': "s1",'x': "s1",
			'y': "s1",'z': "s1",'A': "s1",'B': "s1",'C': "s1",'D': "s1",'E': "s1",'F': "s1",'G': "s1",'H': "s1",'I': "s1",'J': "s1",
			'K': "s1",'L': "s1",'M': "s1",'N': "s1",'O': "s1",'P': "s1",'Q': "s1",'R': "s1",'S': "s1",'T': "s1",'U': "s1",'V': "s1",
			'W': "s1",'X': "s1",'Y': "s1",'Z': "s1"},
		"s1": {'a': "s2",'b': "s2",'c': "s2",'d': "s2",'e': "s2",'f': "s2",'g': "s2",'h': "s2",'i': "s2",'j': "s2",'k': "s2",'l': "s2",
			'm': "s2",'n': "s2",'o': "s2",'p': "s2",'q': "s2",'r': "s2",'s': "s2",'t': "s2",'u': "s2",'v': "s2",'w': "s2",'x': "s2",
			'y': "s2",'z': "s2",'A': "s2",'B': "s2",'C': "s2",'D': "s2",'E': "s2",'F': "s2",'G': "s2",'H': "s2",'I': "s2",'J': "s2",
			'K': "s2",'L': "s2",'M': "s2",'N': "s2",'O': "s2",'P': "s2",'Q': "s2",'R': "s2",'S': "s2",'T': "s2",'U': "s2",'V': "s2",
			'W': "s2",'X': "s2",'Y': "s2",'Z': "s2",'0': "s2",'1': "s2",'2': "s2",'3': "s2",'4': "s2",'5': "s2",'6': "s2",'7': "s2",
			'8': "s2",'9': "s2",},
		"s2": {'a': "s2",'b': "s2",'c': "s2",'d': "s2",'e': "s2",'f': "s2",'g': "s2",'h': "s2",'i': "s2",'j': "s2",'k': "s2",'l': "s2",
			'm': "s2",'n': "s2",'o': "s2",'p': "s2",'q': "s2",'r': "s2",'s': "s2",'t': "s2",'u': "s2",'v': "s2",'w': "s2",'x': "s2",
			'y': "s2",'z': "s2",'A': "s2",'B': "s2",'C': "s2",'D': "s2",'E': "s2",'F': "s2",'G': "s2",'H': "s2",'I': "s2",'J': "s2",
			'K': "s2",'L': "s2",'M': "s2",'N': "s2",'O': "s2",'P': "s2",'Q': "s2",'R': "s2",'S': "s2",'T': "s2",'U': "s2",'V': "s2",
			'W': "s2",'X': "s2",'Y': "s2",'Z': "s2",'0': "s2",'1': "s2",'2': "s2",'3': "s2",'4': "s2",'5': "s2",'6': "s2",'7': "s2",
			'8': "s2",'9': "s2",},
	}
	M3_start_state = 's0'
	M3_accept_states = {'s1','s2'}
	M3_fa = FA(M3_states, M3_transitions, M3_start_state, M3_accept_states)
	M3_strings = ["Ʌ", "HelloWorld", "abc", "1st_Ex", "Java", "the_num", "code", "X3Y7", "X=90", "X*Y"]

	#An FA (M4) which recognizes the set of all decimal unsigned integer numbers without leading zeros except
	#the number 0 (i.e. number 0 should be accepted while number 01 should be rejected.)
	#Setting M4 states transistions, start_state, accept_state
	M4_states = {"s0", "s1", "s2"}  # Define the states
	M4_transitions = {
		"s0": {"0": "s1", "1": "s2", "2": "s2", "3": "s2", "4": "s2", "5": "s2", "6": "s2", "7": "s2", "8": "s2", "9": "s2", ".":"s2"},
		"s1": {"0": "s1"},
		"s2": {"0": "s2", "1": "s2", "2": "s2", "3": "s2", "4": "s2", "5": "s2", "6": "s2", "7": "s2", "8": "s2", "9": "s2", ".":"s2"},
	}
	M4_start_state = "s0"
	M4_accept_states = {"s1","s2"}
	M4_fa = FA(M4_states, M4_transitions, M4_start_state, M4_accept_states)
	M4_strings = ["-7", "007", "3.14", "103", "24930000", "0", "01", "100", "0101"]



	#printing results of each test. 
	print("----------- Testing M1 -----------")
	for string in M1_strings:
		print("The string " + string + " was " + str(M1_fa.recognize(string)))

	print("----------- Testing M2 -----------")
	for string in M2_strings:
		print("The string " + string + " was " + str(M2_fa.recognize(string)))

	print("----------- Testing M3 -----------")
	for string in M3_strings:
		print("The string " + string + " was " + str(M3_fa.recognize(string)))

	print("----------- Testing M4 -----------")
	for string in M4_strings:
		print("The string " + string + " was " + str(M4_fa.recognize(string)))

	#User input variant of code.


	amount_of_states = int(input("enter amount of states: "))
	user_states = set()
	user_transitions = dict()
	for state in range(amount_of_states):
		user_states.add("s" + str(state))
		temp_transistions= dict()
		print("Enter amount of transistions for s" + str(state) + ": ")
		amount_of_transistions = int(input())
		for i in range(amount_of_transistions):
			input_string = input("Enter character: ")
			input_state = input("Enter state: ")
			temp_transistions[input_string] = input_state
		user_transitions["s"+ str(state)] = temp_transistions
		
	user_start_state = input("Enter start state: ")
	

	user_accept_state = set()
	while True:
		value = input("Enter a accept state (type 'done' to exit) (EXAMPLE = ""s0"" or ""s1"" or ""s3""): ")
		if value.lower() == 'done':
			break
		user_accept_state.add(value)



	user_fa = FA(user_states, user_transitions, user_start_state, user_accept_state)

	user_strings = []

	while True:
		value = input("Enter a string test case(type 'done' to exit): ")
		if value.lower() == 'done':
			break
		user_strings.append(value)

	print("----------- Testing M5 -----------")
	for string in user_strings:
		print("The string " + string + " was " + str(user_fa.recognize(string)))

if __name__=="__main__":
	main()