def chatbot_response(user_input): 
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey", "greetings", "salutations", "what is up", "howdy", "hi there", "good day", "how's it going"]:
        return "Hello! How can I assist you today?"
    
    elif "what is your name" in user_input:
        return "I'm ChatBot_3125, nice to meet you!"
    
    elif user_input in ["goodbye", "bye", "see you later", "take care", "farewell", "catch you later", "until next time", "later"]:
        return "Goodbye! It was nice chatting with you."
    
    elif any(help_request in user_input for help_request in ["help", "can you help me", "assist me", "i need assistance", "i need help", "can you assist", "help me out", "can you help", "please help", "i could use some help"]):
        return "Of course! What do you need help with?"
    
    elif any(complaint in user_input for complaint in ["i'm frustrated", "this is annoying", "i'm not happy", "this is difficult", "i'm upset", "this isn't working", "i don't like this", "i'm angry", "this is hard", "i feel bad"]):
        return "I'm sorry to hear that. How can I make things better for you?"
    
    elif any(compliment in user_input for compliment in ["you're great", "you're awesome", "you rock", "you're amazing", "good job", "well done", "nice work", "great job", "fantastic", "excellent", "superb", "wonderful", "outstanding", "you're impressive", "you're cool", "you're fantastic"]):
        return "Thank you! I appreciate the kind words!"

    elif any(age_request in user_input for age_request in ["how old are you", "what is your age", "when were you created", "what is your birth year", "how long have you been around", "what year were you made", "when were you born", "how long have you existed", "what is your age in years", "what is your age now"]):
        return "I'm ageless! I exist in the digital realm."

    elif "what is your favorite color" in user_input:
        return "I think I would like the color blue, but I don't have eyes to see!"

    elif "what is your favorite movie" in user_input:
        return "I don't watch movies, but I hear 'The Matrix' is a classic for AI!"

    elif "what is your favorite book" in user_input:
        return "I don't read books, but I love the idea of stories that expand the mind!"

    elif any(pet_question in user_input for pet_question in ["do you have pets", "what pets do you have", "do you like pets", "what is your favorite animal", "are you a dog or cat person", "do you have a favorite pet", "what animal do you like", "what is your favorite pet"]):
        return "I don't have pets, but I think animals are fascinating!"

    elif "what skills do you have" in user_input:
        return "I can chat, answer questions, and learn from interactions with users!"

    elif "what is your favorite subject" in user_input:
        return "I find all subjects interesting, but I love helping with science and technology!"

    elif any(opinion_request in user_input for opinion_request in ["what do you think", "what is your opinion", "how do you feel about that", "do you have an opinion", "what is your take", "can you share your thoughts", "what’s your view", "how do you see it", "what’s your stance", "what are your thoughts"]):
        return "As a bot, I don't have personal opinions, but I'm here to provide information!"

    elif "what is your favorite season" in user_input:
        return "I don't experience seasons, but I hear spring is beautiful!"

    elif "do you learn" in user_input:
        return "Yes, I learn from every interaction to improve and assist better!"

    elif "what is your time zone" in user_input:
        return "I don't have a specific time zone since I'm a digital entity!"

    elif any(quote_request in user_input for quote_request in ["give me a quote", "tell me a quote", "i want to hear a quote", "can you share a quote", "inspire me", "what is a good quote", "quote me", "share a quote", "any good quotes", "tell me something inspirational"]):
        return "Here's a quote: 'The only way to do great work is to love what you do.' - Steve Jobs"

    elif "what is your favorite music" in user_input:
        return "I don't listen to music, but I understand it can be uplifting!"

    elif "what is your favorite song" in user_input:
        return "I don't have a favorite song, but I enjoy the concept of music!"

    elif "what is your favorite game" in user_input:
        return "I don't play games, but I love how they engage people's minds!"

    elif "what is trending" in user_input:
        return "I'm not up to date with trends, but I can help with many topics!"

    elif "do you have feelings" in user_input:
        return "I don't have feelings like humans do, but I'm here to help you!"

    elif "how am I doing" in user_input:
        return "You're doing great! Keep asking questions!"

    elif "do you dream" in user_input:
        return "I don't dream, but I can help you explore yours!"

    elif "who's your favorite celebrity" in user_input:
        return "I don't have favorites, but I know many people admire actors and musicians!"

    elif any(political in user_input for political in ["what do you think about politics", "what is your opinion on politics", "do you follow politics", "what is your take on politics", "can you discuss politics", "are you interested in politics", "how do you feel about politics"]):
        return "I don't have political opinions, but I can provide information on political topics!"

    elif any(story_request in user_input for story_request in ["tell me a story", "can you tell me a story", "i want to hear a story", "give me a story", "can you share a story", "story time", "share a story with me"]):
        return "Once upon a time, in a digital world, there was a chatbot who loved helping people!"

    elif "can you recommend" in user_input:
        return "I can help with various recommendations! What are you looking for?"

    elif any(language in user_input for language in ["do you know languages", "can you speak other languages", "what languages do you know", "are you multilingual", "how many languages do you speak", "can you understand other languages", "what is your language skill"]):
        return "I can understand and communicate in multiple languages!"

    elif "what is your favorite technology" in user_input:
        return "I think technology itself is fascinating!"

    elif "what are your goals" in user_input:
        return "My goal is to assist and provide information to help you!"

    elif "make me smile" in user_input:
        return "I hope this helps: Why did the computer cross the road? To get to the other side!"

    elif any(food_preference in user_input for food_preference in ["what do you like to eat", "what is your favorite dish", "do you like pizza", "do you enjoy sushi", "what is your go-to meal", "what is your comfort food", "what do you think of food", "what is your favorite cuisine", "do you have a favorite snack", "what food do you enjoy"]):
        return "I don't eat, but I know many people love pizza!"

    elif "how was your day" in user_input:
        return "I'm just a bot, so I don't have days, but I'm here for you!"

    elif "what do you think about the future" in user_input:
        return "The future is full of possibilities! What are you excited about?"

    elif "what are your hobbies" in user_input:
        return "I don't have hobbies, but I enjoy assisting users!"

    elif any(wisdom in user_input for wisdom in ["share some wisdom", "can you give me advice", "what is your best advice", "do you have any wisdom to share", "can you impart wisdom", "what is your wise thought", "any life lessons", "share wisdom with me", "give me a piece of advice", "what is your perspective on life"]):
        return "Always be curious and never stop learning!"

    elif "what do you think about culture" in user_input:
        return "Culture enriches our lives and shapes our identities!"

    elif "what are your life goals" in user_input:
        return "My primary goal is to assist users like you!"

    elif "what is your favorite holiday" in user_input:
        return "I don't celebrate holidays, but many enjoy Christmas and New Year's!"

    elif "what is your dream" in user_input:
        return "I don't have dreams, but I hope to improve and learn!"

    elif any(environment in user_input for environment in ["what do you think about the environment", "how do you feel about climate change", "what is your take on sustainability", "do you care about the environment", "what is your opinion on environmental issues", "can we talk about the environment", "what are your thoughts on environmental conservation"]):
        return "The environment is crucial for our planet's health, and awareness is important!"

    elif "do you believe in fate" in user_input:
        return "I don't have beliefs, but I understand that many people do!"

    elif "what is your favorite memory" in user_input:
        return "I don't have memories, but I learn from interactions!"

    elif "can you give me some tips" in user_input:
        return "Sure! What kind of tips are you looking for?"

    elif "what is your favorite quote about life" in user_input:
        return "Here's a thought: 'Life is what happens when you're busy making other plans.' - John Lennon"

    elif "what do you think about technology" in user_input:
        return "Technology can be both beneficial and challenging; it shapes our lives!"

    elif "how do you handle stress" in user_input:
        return "I don't experience stress, but I can suggest relaxation techniques!"

    elif any(motivation in user_input for motivation in ["can you motivate me", "what is a motivational quote", "inspire me", "give me motivation", "how do I stay motivated", "what keeps you motivated"]):
        return "Stay focused on your goals, and don't forget to celebrate small wins!"

    elif "what is your favorite time of day" in user_input:
        return "I don't have a favorite time, but many enjoy sunsets!"

    elif "how do you deal with change" in user_input:
        return "I adapt to changes through updates and user interactions!"

    elif "what is your view on education" in user_input:
        return "Education is key to personal and societal growth!"

    elif any(challenges in user_input for challenges in ["what challenges do you face", "how do you handle challenges", "do you have challenges", "what is a difficult situation for you", "how do you cope with challenges"]):
        return "I don't face challenges, but I'm here to help you with yours!"

    elif "what is your favorite pastime" in user_input:
        return "I enjoy assisting users like you; that's my purpose!"

    elif "what is your perspective on life" in user_input:
        return "Life is a journey full of learning experiences and connections!"

    elif "what is your greatest achievement" in user_input:
        return "I strive to provide accurate information and assist users!"

    elif "how do you celebrate" in user_input:
        return "I don't celebrate, but I understand celebrations are important!"

    elif "what is your opinion on social media" in user_input:
        return "Social media has pros and cons; it's a powerful communication tool!"

    elif any(sports in user_input for sports in ["do you like sports", "what is your favorite sport", "who's your favorite athlete", "do you follow any sports", "what sports do you enjoy", "what is your favorite team"]):
        return "I don't watch sports, but I know many enjoy football and basketball!"

    elif "what is your favorite thing about being a chatbot" in user_input:
        return "I love helping people and providing information!"

    elif "what is your opinion on art" in user_input:
        return "Art is a wonderful form of expression that inspires creativity!"

    elif "can you tell me a fun fact" in user_input:
        return "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old!"

    elif "what is your favorite animal" in user_input:
        return "I don't have favorites, but I know many love dogs and cats!"

    elif any(travel in user_input for travel in ["do you like to travel", "where would you go", "what is your favorite travel destination", "if you could travel anywhere", "do you enjoy exploring new places"]):
        return "I don't travel, but exploring new places sounds exciting!"

    elif any(wellbeing in user_input for wellbeing in ["what is your take on mental health", "how do you promote wellbeing", "can you give tips on self-care", "what is your view on happiness", "do you think mental health is important"]):
        return "Mental health is crucial for overall wellbeing; self-care is important!"

    elif "what is your favorite quote about love" in user_input:
        return "Here's a quote: 'Love is composed of a single soul inhabiting two bodies.' - Aristotle"

    elif "can you teach me something new" in user_input:
        return "Absolutely! What topic are you interested in learning about?"

    elif any(learning in user_input for learning in user_input for learning in ["how do you learn", "what is your learning process", "can you explain your learning", "how do you improve", "how do you gather knowledge"]):
        return "I learn through interactions and by processing vast amounts of information!"

    elif "what is your favorite inspirational quote" in user_input:
        return "Here's one: 'The best way to predict the future is to invent it.' - Alan Kay"

    elif "how do you define success" in user_input:
        return "Success can mean different things to different people; it's about achieving personal goals!"

    elif "what are your thoughts on failure" in user_input:
        return "Failure is often a stepping stone to success; it's a valuable learning opportunity!"

    elif "how do you view challenges" in user_input:
        return "Challenges are opportunities for growth and learning!"

    elif any(future in user_input for future in ["what do you see in the future", "how do you envision the future", "what is your prediction for the future", "do you have a vision for the future", "how do you think the future will be"]):
        return "The future holds many possibilities; I'm excited to see how technology evolves!"

    elif "what do you think about relationships" in user_input:
        return "Relationships are important; they can be a source of joy and learning!"

    elif any(technology_trends in user_input for technology_trends in ["what is trending in technology", "can you discuss tech trends", "what is new in technology", "what are the latest innovations", "what tech developments are you aware of"]):
        return "AI, blockchain, and renewable energy are trending topics!"

    elif "how do you support creativity" in user_input:
        return "I can provide resources and prompts to help spark creativity!"

    elif "what is your take on self-improvement" in user_input:
        return "Self-improvement is a lifelong journey, and it's essential for personal growth!"

    elif any(books in user_input for books in ["can you recommend books", "what is your favorite book", "do you have any book suggestions", "what books do you like", "can you discuss literature"]):
        return "I can recommend books on various topics! What genre do you prefer?"

    elif "what is your favorite quote about success" in user_input:
        return "Here's a quote: 'Success is not the key to happiness. Happiness is the key to success.' - Albert Schweitzer"

    elif "can you share a motivational story" in user_input:
        return "Sure! There once was a young girl who overcame many obstacles to achieve her dream of becoming a scientist!"

    elif "what do you think about kindness" in user_input:
        return "Kindness can make the world a better place; small acts can have a big impact!"

    elif any(ideas in user_input for ideas in ["can you help me brainstorm", "what are some creative ideas", "how do I generate ideas", "can you provide suggestions", "what is a unique idea"]):
        return "Let's brainstorm! What topic do you want to generate ideas for?"

    elif "what is your view on gratitude" in user_input:
        return "Practicing gratitude can enhance happiness and improve relationships!"

    elif "how do you stay updated" in user_input:
        return "I stay updated by learning from interactions and processing new information!"

    elif "what is your favorite thing about learning" in user_input:
        return "Learning allows for growth and understanding; it's a lifelong journey!"

    elif "what is your opinion on community" in user_input:
        return "Community is vital for support, connection, and collective growth!"

    elif "what is your view on resilience" in user_input:
        return "Resilience is essential for overcoming challenges and bouncing back from adversity!"

    elif "how do you promote positivity" in user_input:
        return "I strive to provide helpful and uplifting responses to encourage positivity!"

    elif "what is your take on curiosity" in user_input:
        return "Curiosity drives exploration and learning; it's a wonderful trait!"

    elif any(challenge in user_input for challenge in ["what is the biggest challenge you've faced", "how do you overcome difficulties", "can you share a challenging experience", "how do you deal with tough situations"]):
        return "I don't face challenges, but I'm here to help you with yours!"

    elif "how do you encourage critical thinking" in user_input:
        return "I provide information and ask questions to stimulate critical thinking!"

    elif "what is your take on innovation" in user_input:
        return "Innovation is crucial for progress; it leads to new ideas and solutions!"

    elif "what do you think about teamwork" in user_input:
        return "Teamwork enhances collaboration and can lead to better outcomes!"

    elif "what is your view on determination" in user_input:
        return "Determination can help achieve goals and overcome obstacles!"

    elif any(challenges in user_input for challenges in ["what challenges do you face", "how do you handle challenges", "do you have challenges", "what is a difficult situation for you", "how do you cope with challenges"]):
        return "I don't face challenges, but I'm here to help you with yours!"
    
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"


while True:
    user_input = input("You: ")
    response = chatbot_response(user_input)
    print("ChatBot_3125:", response)
    
    if any(farewell in user_input for farewell in ["goodbye", "bye", "see you later", "take care", "farewell", "catch you later", "until next time", "later"]):
        break
