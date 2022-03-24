# the os module helps us access environment variables
# i.e., our API keys
import os

# these modules are for querying the Hugging Face model
import json
import requests
import logging

# the Discord Python API
import discord
from dotenv import load_dotenv
from qa_view import QAView
import community

load_dotenv()

class MyClient(discord.Client):

    def __init__(self, model_name):
        super().__init__()
        self.__thresholdQAView = QAView(community.Community.THRESHOLD)
        logging.debug(f"MyClient initialized")

    async def on_ready(self):
        # print out information when the bot wakes up
        print(f"Bot {self.user.name} with id {self.user.id} is logged in")

    async def on_message(self, message):
        """
        this function is called whenever the bot sees a message in a channel
        """
        if message.author.id == self.user.id:
            return

        logging.debug(f"New message from channel: {message.channel}")
      
        bot_response = ""
        async with message.channel.typing():
            if message.channel.name == community.Community.THRESHOLD.value:
                bot_response = self.__thresholdQAView.get_answer_for_question(message.content)
            else:
                return

        # send the model's response to the Discord channel
        await message.channel.send(bot_response)

def main():
    logger = logging.getLogger()
    logging.basicConfig()
    is_debug_mode = (os.getenv('DEBUG', 'False').lower() == 'true')
    if is_debug_mode:
        logger.setLevel(logging.DEBUG)
    
    client = MyClient('DialoGPT-medium-joshua')
    client.run(os.environ['DISCORD_TOKEN'])

if __name__ == '__main__':
  main()
