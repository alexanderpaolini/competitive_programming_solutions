# Submitted
def hamming_distance(string1: str, string2: str):
    """Return the Hamming distance between two strings."""
    if len(string1) != len(string2):
        return 1e99
    dist_counter = 0
    for n in range(len(string1)):
        if string1[n] != string2[n]:
            dist_counter += 1
    return dist_counter


num_cases = int(input())

for _ in range(num_cases):
    num_dict, num_wrong = map(int, input().split())

    words_dict = []
    for _ in range(num_dict):
        words_dict.append(input())

    for word_index in range(num_wrong):
        curr_word = input()
        min_dist = 1e99
        min_index = -1
        for i, correct_word in enumerate(words_dict):
            curr_dist = hamming_distance(curr_word, correct_word)
            if curr_dist < min_dist:
                min_dist = curr_dist
                min_index = i
        print(words_dict[min_index])
