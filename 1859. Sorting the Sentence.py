class Solution:
    def sortSentence(self, s: str) -> str:
        shuffled_sentence = s.split(" ")
        print(shuffled_sentence)
        Correct_sentence = ""
        for i in range(len(shuffled_sentence)):
            min_position = i
            for j in range(i+1, len(shuffled_sentence)):
                if shuffled_sentence[j][-1]< shuffled_sentence[min_position][-1]:
                    min_position= j
            if i!= min_position:
                shuffled_sentence[min_position], shuffled_sentence[i] =shuffled_sentence[i] , shuffled_sentence[min_position]
            Correct_sentence+= shuffled_sentence[i][:-1]+" "
        return (Correct_sentence[ :-1])
