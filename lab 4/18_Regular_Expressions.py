import re

def test_email(your_pattern):
    pattern = re.compile(your_pattern)
    emails = ["john@example.com", "python-list@python.org",
              "wha.t.`1an?ug{}ly@email.com"]
    for email in emails:
        if re.fullmatch(pattern, email):
            print("Pass")
        else:
            print("You failed to match %s" % email)

pattern = r"[A-Za-z0-9.`?{}_-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+"
test_email(pattern)
