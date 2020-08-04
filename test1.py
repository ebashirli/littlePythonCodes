# Sışxıdırılmaq istənilən mətn
mtn = '''
Once upon a time, long, long ago, three little pigs set out to make their fortunes. The first little pig wasn’t very clever, and decided to build his house out of straw, because it was cheap. The second little pig wasn’t very clever either, and decided to build his house out of sticks, for the “natural” look that was so very much in fashion, even in those days. The third little pig was much smarter than his two brothers, and bought a load of bricks in a nearby town, with which to construct a sturdy but comfortable country home.
Not long after his housewarming party, the first little pig was curled up in a chair reading a book, when there came a knock at the door. It was the big bad wolf, naturally.
“Little pig, little pig, let me come in!” cried the wolf.
“Not by the hair on my chinny-chin-chin!” squealed the first little pig.
“Then I’ll huff, and I’ll puff, and I’ll blow your house down!” roared the wolf, and he did huff, and he did puff, and the house soon collapsed. The first little pig ran as fast as he could to the house of sticks, and was soon safe inside. But it wasn’t long before the wolf came calling again.
“Little pig, little pig, let me come in!” cried the wolf.
“Not by the hair on my chinny-chin-chin!” squealed the second little pig.
“Then I’ll huff, and I’ll puff, and I’ll blow your house down!” roared the wolf, and he did huff, and he did puff, and the house was soon so much firewood. The two terrified little pigs ran all the way to their brother’s brick house, but the wolf was hot on their heels, and soon he was on the doorstep.
“Little pig, little pig, let me come in!” cried the wolf.
“Not by the hair on my chinny-chin-chin!” squealed the third little pig.
“Then I’ll huff, and I’ll puff, and I’ll blow your house down!” roared the wolf, and he huffed, and he puffed, and he huffed some more, but of course, the house was built of brick, and the wolf was soon out of breath. Then he had an idea. The chimney! He clambered up a handy oak tree onto the roof, only to find that there was no chimney, because the third little pig, being conscious of the environment, had installed electric heating. In his frustration, the wolf slipped and fell off the roof, breaking his left leg, and severely injuring his pride. As he limped away, the pigs laughed, and remarked how much more sensible it was to live in the city, where the only wolves were in the zoo. And so that is what they did, and of course they all lived happily ever after.
'''

# Mətnin sıxıışdırılmamış uzunluğu
uz = len(mtn)

# Mətnin sıxıışdırılmamış uzunluğunun yarısının tam hissəsi
i = int(uz/2)

while i >= 2:
    # Əvvəldə olub-olmadığının yoxlanması üçün götürülmüş mətn hissəsinin ilk indeksi
    j = 0
    while 2 * i + j <= len(mtn):
        # Mətnin əvvəlindən əvvəldə olub-olmadığının yoxlanması üçün götürülmüş mətn hissəsinin son indeksinədək olan mətn hissəsi
        a = mtn[: i + j]
	
	# Əvvəldə olub-olmadığının yoxlanması üçün götürülmüş mətn hissəsi
        b = mtn[i+j : 2 * i + j]
        if b in a:
          mtn = mtn[: i+j] + mtn[i+j+i:]
        j+=1
        
    i-=1

# Silinmiş simvol sayını çap et
print(uz - len(mtn))

# Sıxışdırılmış mətni çap et
print('Sıxışdırılmış mətn:\n', mtn)
