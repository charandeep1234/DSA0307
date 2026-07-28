def check(subject, verb):

    singular = ["he", "she", "it"]
    plural = ["they", "we", "you"]

    if subject.lower() in singular and verb.endswith("s"):
        print("Correct Agreement")

    elif subject.lower() in plural and not verb.endswith("s"):
        print("Correct Agreement")

    else:
        print("Incorrect Agreement")

subject = input("Enter Subject: ")
verb = input("Enter Verb: ")

check(subject, verb)
