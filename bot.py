
import discord, random, os, requests
from  bot_logic import color, gen_pass, get_random_emoji, get_random_roast, ideas, color
from bot_logic import pickup_line, compliment

print(os.listdir('images'))

# intents variable stores the permissions of the bot
intents = discord.Intents.default()
# Enable the permission to read message content
intents.message_content = True
# Create a bot and pass the intents
client = discord.Client(intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'): 
        await message.reply(('Hello '+str(message.author)+'!'), mention_author=True)
    elif message.content.startswith('$bye'):
        await message.channel.send("\U0001f642", mention_author=True)
    elif message.content.startswith('$generate'):
        parts = message.content.split()

        if len(parts) == 2 and parts[1].isdigit():
            pass_length = int(parts[1])
            password = gen_pass(pass_length)
            await message.channel.send("Generated password: " + password)
            await message.channel.send("The generated password was " + str(len(password)) + " characters long.")
        else:
            await message.channel.send("Use $generate followed by a number, e.g. $generate 12")
    elif message.content.startswith('$emoji'):
        emoji = get_random_emoji()
        await message.channel.send(emoji)
    elif message.content.startswith("$8ball"):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        response = random.choice(responses)
        await message.channel.send(response)
    elif message.content.startswith("$rps"):
        choices = ["rock", "paper", "scissors"]
        user_choice = message.content.split()[1].lower()
        if user_choice not in choices:
            await message.channel.send("Invalid choice! Please format your command as $rps <rock/paper/scissors>.")
            return
        bot_choice = random.choice(choices)
        await message.channel.send("You chose " + user_choice + ", I chose " + bot_choice + ".")
        if user_choice == bot_choice:
            await message.channel.send("It's a tie!")
        elif (user_choice == "rock" and bot_choice == "scissors") or (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
            await message.channel.send("You win!")
        else:
            await message.channel.send("I win!")
    elif message.content.startswith("$coinflip"):
        result = random.choice(["Heads", "Tails"])
        await message.channel.send("The coin landed on: " + result)
    elif message.content.startswith("$help"):
        help_message = (
            "Here are the commands you can use:\n"
            "$hello - Greet the bot\n"
            "$bye - Say goodbye to the bot\n"
            "$generate <length> - Generate a random password of specified length\n"
            "$emoji - Get a random emoji\n"
            "$8ball <question> - Ask the magic 8-ball a question\n"
            "$rps <rock/paper/scissors> - Play rock-paper-scissors with the bot\n"
            "$coinflip - Flip a coin\n"
            "$meme - Get a random meme image\n"
            "$duck - Get a random duck image\n"
            "$roast - Get a random roast\n"
            "$idea - Get a random idea for environmental action\n"
            "$color - Get a random color name\n"
            "$pickup - Get a random pickup line\n"
            "$compliment - Get a random compliment\n"
            "$help - Show this help message"
        )
        await message.channel.send(help_message)
    elif message.content.startswith("$meme"):
        meme = random.choice(['meme1.png', 'meme2.png', 'meme3.png', 'meme4.png', 'meme5.png', 'meme6.png', 'meme7.png', 'meme8.png', 'meme9.png'])
        with open('images/'+meme, 'rb') as f:
            picture = discord.File(f)
            await message.channel.send(file=picture)
    elif message.content.startswith("$duck"):
        image_url = get_duck_image_url()
        await message.channel.send(image_url)
    elif message.content.startswith("$roast"):
        roast = get_random_roast()
        await message.channel.send(roast)
    elif message.content.startswith("$idea"):
        idea = ideas()
        await message.channel.send(idea)
    elif message.content.startswith("$color"):
        random_color = color()
        await message.channel.send(random_color)
    elif message.content.startswith("$pickup"):
        random_pickup_line = pickup_line()
        await message.channel.send(random_pickup_line)
    elif message.content.startswith("$compliment"):
        random_compliment = compliment()
        await message.channel.send(random_compliment)
    else:
        await message.channel.send(message.content)

client.run("YOUR_BOT_TOKEN_HERE")
