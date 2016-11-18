
def findSubSeq(genome, subseq):
    states = [] #store state tuples
    for i in range(0, len(subseq)):
        tup = (i+1, subseq[i]); #use i+1 to get rid of 0 based indexing
        states.append(tup)

    curr_state = 1
    curr_char = states[0][1] #char to look for
    num_states = len(states) #total number of states

    count = 0 #used for indexing later
    
    for char in genome:
        if char == curr_char: #if found char we're looking for
            if curr_state == num_states: #found subseq
                return True
            curr_state+=1 #update state
            curr_char = states[curr_state-1][1] #update curr char looking for
            count+=1

        else:
            s = getState(states, char) #get the prev state
            if (s!=0 and genome[count-1]==states[s-2][1]): #if prev state and prev char match
                curr_state = s+1
                curr_char = states[curr_state-1][1]
                count+=1

            else: #otherwise start over
                curr_state = 1
                curr_char = states[0][1]
                count = 0

        

    return False


def getState(states, char): #find most recent char/state to go back to
    for i in range(len(states)-1, -1, -1):
        if states[i][1] == char:
            return states[i][0]

    return 0
    


print(findSubSeq("CACACAT", "CACAT"))
    




