from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "540bdefd89700adaf8990c20e7d7e161")
      API_ID = int(getenv("API_ID", "20555510"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6921230866:AAF6oR85oxunAQ1_x6kKq2rJRYBzDSTLy-4")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1898954257:-1746906415").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
