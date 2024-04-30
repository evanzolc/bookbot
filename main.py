
# This bring book to this sheet
with open("books/frankenstein.txt") as f:
    frank_book = f.read()
    

# This is a word count of the book
count = 0
for word in frank_book.split():
    
    count += 1



# This will count the number of each indavicual letter in the book all lower case

small_frank_book = frank_book.lower()
letters = {}
letter_list = []
 
for x in small_frank_book:
    if x in letters:
        letters[x] += 1
    else:
        letters[x] = 1

for letter, freq in letters.items():
    if letter.isalpha():
        letter_dict = {"letter": letter, "frequency": freq}
        letter_list.append(letter_dict)

letter_list.sort(key=lambda x: x["frequency"], reverse=True)

print()   
print("--- Begin report of book/frankenstein.txt ---")
print()
print(f"{count} words found in the document")
print()
for item in letter_list:
    print(f"The '{item['letter']}' character was found {item['frequency']} times")
print()
print("--- End report ---")
