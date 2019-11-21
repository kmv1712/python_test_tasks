class Wars:
    health = 100

    def losing_health(self):
        self.health -= 20
        
wars_one, wars_two  = Wars(), Wars()

while wars_one.health and wars_two.health:
    if random.random() < random.random():
        print('Второй воин атаковал первого')    
        wars_one.losing_health() 
    else:
        print('Первый воин атаковал второго')
        wars_two.losing_health()

print("Убит {}".format("первый воин" if not wars_one.health else "второй воин"))
