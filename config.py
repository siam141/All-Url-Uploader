
# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

# edit this file with your veriable if you'r deploy bot via locally | vps

from dotenv import load_dotenv
import os

load_dotenv()

class Config(object):

    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7881581733:AAGxDnk7Uzn7J0d9_WUmGg1Ah8bMz6xYx9A")
    # bot username without @
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MirrorLeach2Bot")

    # Get these values from my.telegram.org
    API_ID = os.environ.get("API_ID", "27752560")
    API_HASH = os.environ.get("API_HASH", "67d3ec64db8031189962b5d4804884c0")

    # TG Ids
    LOG_CHANNEL = os.environ.get("LOG_CHANNEL", "-1002589776901")
    OWNER_ID = os.environ.get("OWNER_ID", "7862181538")
    AUTH_USERS = [OWNER_ID] + os.environ.get("AUTH_USERS", "7862181538").split(" ")

    # No need to change
    ADL_BOT_RQ = {}
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./DOWNLOADS")
    CHUNK_SIZE = os.environ.get("CHUNK_SIZE", 128)
    TG_MAX_FILE_SIZE = os.environ.get("TG_MAX_FILE_SIZE", 4194304000)
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    PROCESS_MAX_TIMEOUT = os.environ.get("PROCESS_MAX_TIMEOUT", 3700)