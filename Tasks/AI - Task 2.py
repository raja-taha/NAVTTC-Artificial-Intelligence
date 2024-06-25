# Tuples
# Question 1
# def pairwise_swap(tup):
#     if len(tup) % 2 != 0:
#         raise ValueError("The tuple must have an even length.")
#     swapped = []
#     for i in range(0, len(tup), 2):
#         swapped.append(tup[i+1])
#         swapped.append(tup[i])
#     return tuple(swapped)
#
# print(pairwise_swap((1, 2, 3, 4)))

# Question 2
# def unzip_tuples(tup_lst):
#     first_elements = ()
#     second_elements = ()
#     for tup in tup_lst:
#         first_elements += (tup[0],)
#         second_elements += (tup[1],)
#     return first_elements, second_elements
#
# print(unzip_tuples(((1, 2), (3, 4))))

# Question 3
# def is_anagram(str1, str2):
#     return sorted(str1) == sorted(str2)
#
# print(is_anagram("taha", "taha"))

# Question 4
# def capitalize_words(sentence):
#     words = sentence.split()
#     capitalized_words = [word.capitalize() for word in words]
#     return ' '.join(capitalized_words)
#
# print(capitalize_words("my name is taha"))

# Question 5
# def compress_string(s):
#     if not s:
#         return s
#
#     compressed = []
#     count = 1
#
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             count += 1
#         else:
#             compressed.append(s[i - 1] + str(count))
#             count = 1
#
#     compressed.append(s[-1] + str(count))  # Add the last group
#
#     compressed_str = ''.join(compressed)
#
#     return compressed_str if len(compressed_str) < len(s) else s
#
# print(compress_string("aaabbcc"))

# Sets
# Question 1
# def find_common_elements(set1, set2):
#     return set1.intersection(set2)
#
# set1 = {1, 2, 3, 4, 5}
# set2 = {3, 4, 5, 6, 7}
# print(find_common_elements(set1, set2))

# Question 2
# def unique_elements(lst):
#     count_dict = {}
#     for elem in lst:
#         if elem in count_dict:
#             count_dict[elem] += 1
#         else:
#             count_dict[elem] = 1
#
#     unique_set = set()
#     for elem, count in count_dict.items():
#         if count == 1:
#             unique_set.add(elem)
#
#     return unique_set
#
# lst = [1, 2, 2, 3, 4, 4, 5, 6, 6]
# print(unique_elements(lst))