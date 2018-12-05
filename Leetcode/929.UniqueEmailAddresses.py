def numUniqueEmails(emails):
        """
        :type emails: List[str]
        :rtype: int
        """

        freq = set([])
        for email in emails:
            username = ""
            domain = ""
            seen_at = False
            seen_plus = False
            seen_dot = False
            for i, char in enumerate(email):

                if char == ".":
                    seen_dot = True
                if char == "@":
                    seen_at = True
                if char == "+":
                    seen_plus = True
                if seen_at:
                    domain += char
                else:
                    if seen_plus:
                        pass
                    else:
                        if char != ".":
                            username += char

            email_address = username + domain
            freq.add(email_address)
        print freq
        return len(freq)

def UsingStringOperators(emails):

    freq = set([])

    for email in emails:

        username, domain  = email.split("@")
        username = username.replace(".", "")
        username = username[:username.index("+")]
        freq.add(username + domain)


    return len(freq)


print UsingStringOperators(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"])
