# This is a method to split a string into as many smaller substrings as possible when each substring is the same string.
# The method returns the number of substrings that is possible from the string.
# The string is like a pie so the end char of the string is before the beggining char of the string. So the beginning of
# the string could be the end of the repeated pattern which started at the end of the string
def solution(sol):

    result = 1
    for iteration in range (len(sol)):  # This shifts the string so after the first iteration the last char becomes the first
        new_sol = sol[iteration:] + sol[:iteration]
        result = checkPattern(new_sol)
        if (result != 1):
            break
    return result

def checkPattern(sol):
    number_of_pieces = 1
    number_of_iterations = 0
    number_of_iterations = int(len(sol) / 2) + 1
    for length_of_substring in range (1, number_of_iterations):
        if (len(sol) % length_of_substring == 0):
            number_of_pieces = int(len(sol) / length_of_substring)
            firstSubstring = sol[0:length_of_substring]
            foundAnswer = True
            for piece in range (number_of_pieces):
                start_positon = piece*length_of_substring
                end_position = length_of_substring+(piece*length_of_substring)
                if(sol[start_positon:end_position] != firstSubstring):
                    foundAnswer = False
                    number_of_pieces = 1
            if (foundAnswer):
                break
    return number_of_pieces   


print(solution("absdefghi")) # 1
print(solution("abababababababab")) #8
print(solution("gggggggggg")) #10
print(solution("cbacbacba")) #3
print(solution("asdfgasdfgasdfgasdfg")) #4
print(solution("abcabcabcabc")) #4
print(solution("abccbaabccba")) #2
print(solution("fabcdefabcde")) #2
print(solution("bcdefabcdefa")) #2
print(solution("cbacbacbaz")) #1
print(solution("zbacbacba")) #1
