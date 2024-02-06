from faker import Faker

fake = Faker()

people = []

for i in range(10):
    ppl = {}
    ppl['name'] = fake.name()
    ppl['email'] = fake.email()
    people.append(ppl)

print(people)
    
    


