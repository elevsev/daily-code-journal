import random

random_facts = [
"Canada's forests make up nearly 9 percent of the world's total forest area.",
"In 1961 two hydrogen bombs were accidentally dropped over North Carolina. A glitch prevented them from detonating. ",
"90 percent of the world's population lives in the Northern Hemisphere.",
"Due to their fur, the polar bear is relatively  'invisible ' to an infrared camera.",
"'Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo ' is a grammatically correct sentence.",
"The US has lost 6 nuclear weapons.",
"The chainsaw was originally created to aid in childbirth.",
"If you could fold a piece of paper in half 42 times, it would reach the moon. ",
"Mark Twain was born on the same day Halley's Comet flew by the earth. He said  'I came in with Halley's Comet in 1835. It is coming again next year, and I expect to go out with it.' Halley's Comet appeared on April 21, 1910, which is the day Mark Twain died.",
"Whale sharks have teeth on their eyeballs.",
"Broccoli, Brussels sprouts, cabbage, cauliflower, collard greens, gai lan, kale, kohlrabi, and savoy are all the same species of plant called  'Brassica oleracea '",
"It's suspected that on Neptune and Uranus, it rains diamonds.",
"There are more trees on earth than stars in the Milky Way galaxy.",
"Australia once lost a war to emus (the birds).",
"A town in Pennsylvania has had an uncontrolled fire burning since 1962.",
"The longest boxing match went 110 rounds and over 7 hours.",
"The national animal of Scotland is the unicorn.",
"The phrase  'hands down ' comes from horseracing. It refers to a jockey who's so far ahead that he can afford to drop his hands and loosen the reins (usually kept tight to encourage a horse to run) and still easily win.",
"You have no major muscles in your fingers. All muscles that control finger movement are in your forearm and palm.",
"In space, you don't need welding materials to get two metals to fuse. They will do it on their own if you place them close enough together.",
]

random_fact_index = random.randint(0,(len(random_facts)))

print("Random fact of the day:")
print("******************************************************************************************************************************************************")
print(random_facts[random_fact_index])
print("******************************************************************************************************************************************************")
