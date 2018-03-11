def index_words(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == " ":
            yield index + 1


if __name__ == '__main__':
    address = "We would like to remind you that you have an interview to be completed for us by February 25, 2018 (23.59 GMT). Interviews cannot be completed after this date and will appear as a non-response from you."
    it = index_words(address)
    print(next(it))
    print(next(it))
    print(next(it))
