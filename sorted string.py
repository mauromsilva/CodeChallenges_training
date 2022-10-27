def sort_words(vstring):
    return(' '.join(sorted(vstring.split(), key=str.casefold)))

print(sort_words(input()))