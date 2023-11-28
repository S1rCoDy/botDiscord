import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import textwrap

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# Things to run when the bot connects to Discord
@bot.event
async def on_ready():
    print('Подключено')

# Test command
@bot.command(pass_context=True)
async def text(ctx, *args):
    # Combine all arguments into a single string
    text_to_add = ' '.join(args)

    # Load the base image
    base_image = Image.open('fon.png')

    # Load the font
    font = ImageFont.truetype('ISOCPEUR_it.ttf', 60)  # Adjust the font size as needed

    # Create a drawing context
    draw = ImageDraw.Draw(base_image)

    # Position to place the text
    text_position = (50, 50)  # Adjust the position as needed

    # Set the text color (black in RGB)
    text_color = (0, 0, 0)

    # Wrap the text to fit within a certain width
    max_width = 974  # Adjust the maximum width as needed
    wrapped_text = textwrap.fill(text_to_add, width=30)  # Adjust the width as needed

    # Add wrapped text to the image
    draw.text(text_position, wrapped_text, font=font, fill=text_color)

    # Save the edited image
    edited_image_path = 'edited_fon.png'
    base_image.save(edited_image_path)

    # Send the edited image to Discord
    await ctx.send(file=discord.File(edited_image_path))

bot.run('MTE3NzkxNDE5MDY0ODg0NDM4OA.GZ3tmF.BCGrb4hWSrQohkEWBeDsCDhxgzMQtG7mm_CN3Q')