def count_words(filename):
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} doesn't exist!")
    else:
        words = contents.split()
        print(f"The file {filename} has about {len(words)} words.")

file_names = ['guest.txt', 'programming.txt', 'responses.txt', 'test.txt']
for file in file_names:
    count_words(file)

