

fname = input('Write your file name: ')
with open(fname) as file:
    d = {}
    domain_counts = {}
    for line in file:
        
            if line.startswith('From'):
                words = line.split()
                email = words[1]
                d[email] = d.get(email, 0) + 1


for email, count in d.items():
    print(email, count)

# Find the email address with the maximum count
max_count = 0
max_email = ''
for email, count in d.items():
    if count > max_count:
        max_count = count
        max_email = email


print("Email address with the most messages:", max_email)
print("Message count:", max_count)

# Extract the domain from the email address
domain = email.split('@')[-1]
domain_counts[domain] = domain_counts.get(domain, 0) + 1

for domain, count in domain_counts.items():
    print(domain, count)