import os
import pyrogram
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

class Config(object):

    START_TEXT = """
<b>👋 ʜᴀʏʏ {}

ɪ ᴀᴍ ᴀ ғɪʟᴇ/ᴠɪᴅᴇᴏ ᴍᴇʀɢᴇʀ ʙᴏᴛ. 

ɪ ᴄᴀɴ ᴍᴇʀɢᴇ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇs!, ᴀɴᴅ ᴜᴘʟᴏᴀᴅ ɪᴛ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴍ. 

ᴍᴏʀᴇ ᴛʜᴀɴ 𝟸ɢʙ ғɪʟᴇ ᴡɪʟʟ sᴘʟɪᴛ ɪɴ ᴘᴀʀᴛs.

ғᴏʀ ᴀᴜᴅɪᴏ, ʙᴇғᴏʀᴇ ᴜsɪɴɢ, ғɪʀsᴛ sᴇᴛ ᴀᴜᴅɪᴏ ǫᴜᴀʟɪᴛʏ ɪɴ /settings

ɪғ ᴀɴʏ ᴇʀʀᴏʀ ᴀᴘᴘᴇᴀʀs, ᴛʜᴇɴ ʀᴇᴘᴏʀᴛ ɪᴛ ᴛᴏ 👉 @Help_Group

ᴄʟɪᴄᴋ ʜᴇʟᴘ ʙᴜᴛᴛᴏɴ ғᴏʀ ᴍᴏʀᴇ ᴅᴇᴛᴀɪʟs.
</b>"""

    FREE_USERS_TXT = """
**𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝗻 𝗗𝗲𝗮𝘁𝗮𝗶𝗹𝘀 :

👤 ᴜsᴇʀ: @{}

🆔 ᴜsᴇʀɪᴅ: `{}`

🏷️ ᴘʟᴀɴ: `Free`

🎯 ᴘʟᴀɴ ᴇɴᴅs ᴏɴ: `Lifetime`

📆 ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ: `{}`**
            """
    PLAN_EXPIRED_1_TXT = """ 
**👤 ᴜsᴇʀ: @{}

🆔 ᴜsᴇʀɪᴅ: `{}`

📆 ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ: `{}`

⏳ ᴘʟᴀɴ ᴠᴀʟɪᴅɪᴛʏ: `{}`

✅ ᴘʟᴀɴ ᴊᴏɪɴᴇᴅ ᴏɴ: `{}`

👋 ʏᴏᴜʀ ᴘʟᴀɴ ʜᴀs ᴇxᴘɪʀᴇᴅ ᴏɴ:
`{}` **
            """
    PLAN_EXPIRED_TXT = """ 
**𝗣𝗹𝗮𝗻 𝗘𝘅𝗽𝗶𝗿𝗲𝗱:

👤 ᴜsᴇʀ: @{}

🆔 ᴜsᴇʀɪᴅ: `{}`

✅ ᴘʟᴀɴ ᴊᴏɪɴᴇᴅ ᴏɴ: `{}`

📆 ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ: `{}`

⏳ ʀᴇᴍᴀɪɴɪɴɢ: `{}`

📑 ᴘʟᴀɴ ᴅɪsᴄʀɪᴘᴛɪᴏɴ : `{}`**
            """
    PAID_USERS_TXT = """
**𝗬𝗼𝘂𝗿 𝗣𝗹𝗮𝗻 𝗗𝗲𝗮𝘁𝗮𝗶𝗹𝘀 :

👤 ᴜsᴇʀ: @{}

🆔 ᴜsᴇʀɪᴅ: `{}`

🏷️ ᴘʟᴀɴ: `paid`

✅ ᴘʟᴀɴ sᴛᴀʀᴛᴇᴅ ᴏɴ: `{}`

🎯 ᴘʟᴀɴ ᴇɴᴅs ᴏɴ: `{}`

📆 ᴛᴏᴅᴀʏ ᴅᴀᴛᴇ: `{}`

⏳ ʀᴇᴍᴀɪɴɪɴɢ: `{}`

📑 ᴘʟᴀɴ ᴅɪsᴄʀɪᴘᴛɪᴏɴ : `{}`**
            """

    BAN_TXT = """
__Sᴏʀʀʏ Sɪʀ, Yᴏᴜ ᴀʀᴇ Bᴀɴɴᴇᴅ ᴛᴏ ᴜsᴇ ᴍᴇ. __

**Cᴏɴᴛᴀᴄᴛ [Sᴜᴘᴘᴏʀᴛ Gʀᴏᴜᴘ](https://t.me/kr_join) Tʜᴇʏ Wɪʟʟ Hᴇʟᴘ Yᴏᴜ**
"""

    PAID_JOIN_TXT = """
**🏷 Plan: Free 🆓

⌾ Daily Bypass: False

🏷 Plan: Premium 🏆

⌾ Daily Bypass: Unlimited
⌾ Daily Scrape: Unlimited
⌾ More Additions Coming Soon...

💰 1 Month: ₹15 
💰 2 Months: ₹25
💰 3 Months: ₹40
💰 6 Months: ₹80
💰 12 Months: ₹160

💳 Pay using UPI ID `tamildub@ybl`

🧾 After payment, send screenshots of the payment to the admin to activate your plan.

📌 NOTE: Before paying, check if the admin is active or not!**
    """


    HELP_TEXT = """
<b>🎆 𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘 𝗕𝗬𝗣𝗔𝗦𝗦𝗘𝗥 𝗕𝗢𝗧

𝖳𝗁𝗂𝗌 𝖡𝗈𝗍 𝖢𝖺𝗇 𝖡𝗒𝗉𝖺𝗌𝗌 𝖠𝖽𝗌 𝖫𝗂𝗇𝗄 𝖠𝗇𝖽 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖣𝗂𝗋𝖾𝖼𝗍 𝖫𝗂𝗇𝗄𝗌.

𝖨 𝖼𝖺𝗇 𝖡𝗒𝗉𝖺𝗌𝗌 𝖬𝖺𝗇𝗒 𝖲𝗁𝗈𝗋𝗍𝗇𝖾𝗋𝗌 𝖫𝗂𝗇𝗄𝗌 𝖠𝗅𝗌𝗈 𝖨 𝖼𝖺𝗇 𝖦𝖾𝗇𝖾𝗋𝖺𝗍𝖾 𝖣𝗂𝗋𝖾𝖼𝗍 𝖫𝗂𝗇𝗄𝗌 𝖥𝗈𝗋 𝖬𝖾𝖽𝗂𝖺𝖿𝗂𝗋𝖾, 𝖹𝗂𝗉𝗉𝗒𝗌𝗁𝖺𝗋𝖾, 𝖤𝗍𝖼 

𝖲𝖾𝗇𝖽 /sites 𝖳𝗈 𝖲𝖾𝖾 𝖲𝗎𝗉𝗉𝗈𝗋𝗍𝖾𝖽 𝖲𝗂𝗍𝖾𝗌

♥️Made By - @MrTamilKiD

⚜️ 𝙞𝙛 𝘽𝙤𝙩 𝙉𝙤𝙩 𝙒𝙤𝙧𝙠𝙞𝙣𝙜 𝘼𝙣𝙙 𝙞𝙨𝙨𝙪𝙚𝙨 𝘾𝙤𝙣𝙩𝙖𝙘𝙩 
𝗔𝗱𝗺𝗶𝗻 : @KR_Admin_Bot
𝗨𝗽𝗱𝗮𝘁𝗲 : @KR_Botz </b>
"""

    ABOUT_TEXT = """
<b>╔════❰ 𝗕𝗬𝗣𝗔𝗦𝗦𝗘𝗥 𝗕𝗢𝗧 ❱═══❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖 Mʏ Nᴀᴍᴇ : <a href='https://t.me/KRLinkBypasserBOt'>『 Link Bypasser BOt 』</a>
║┣⪼👦 Oᴡɴᴇʀ : <a href=https://t.me/MR_tamil_kid>Tค๓เl ᠰ TɢX</a>
║┣⪼👨‍💻 Dᴇᴠ : @MrTamilKiD
║┣⪼📢 Uᴘᴅᴀᴛᴇ : <a href=https://t.me/kr_botz>𝗞𝗥 ⚠︎ 𝗕ᴏᴛᴢ</a>
║┣⪼❣️ Sᴜᴘᴘᴏʀᴛ : <a href=https://t.me/kr_join>𝗞𝗥 👽 𝗝ᴏɪɴ</a>
║┣⪼📡 Sᴇʀᴠᴇʀ : <a href=https://www.heroku.com>Hᴇʀᴏᴋᴜ Eᴄᴏ</a>
║┣⪼🗣️ Lᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Pʏᴛʜᴏɴ3</a>
║┣⪼📚 Lɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pʏʀᴏɢʀᴀᴍ</a>  
║┣⪼🗒️ Vᴇʀsɪᴏɴ : V 1.0.0 [ Bᴇᴛᴀ ]
║╰━━━━━━━━━━━━━━━➣
╚═════❰ @KR_Botz ❱═════❍ </b>
"""
    DON_TXT = """
<b><u>💗 𝐓𝐡𝐚𝐧𝐤𝐬 𝐟𝐨𝐫 𝐬𝐡𝐨𝐰𝐢𝐧𝐠 𝐢𝐧𝐭𝐞𝐫𝐞𝐬𝐭 𝐢𝐧 𝐝𝐨𝐧𝐚𝐭𝐢𝐨𝐧</u>

Dᴏɴᴀᴛᴇ Us Tᴏ Kᴇᴇᴘ Oᴜʀ Sᴇʀᴠɪᴄᴇs Cᴏɴᴛɪɴᴏᴜsʟʏ Aʟɪᴠᴇ 😢
Yᴏᴜ Cᴀɴ Sᴇɴᴅ Aɴʏ Aᴍᴏᴜɴᴛ 
Dᴏɴᴀᴛᴇ Oɴʟʏ Oɴᴇ Rᴜᴘᴇᴇ 🥲
Of 10₹, 20₹, 30₹, 50₹, 70₹, 100₹, 200₹ 😊
📨 Pᴀʏᴍᴇɴᴛ Mᴇᴛʜᴏᴅs:
 
GᴏᴏɢʟᴇPᴀʏ / Pᴀʏᴛᴏɴ / PʜᴏɴPᴀʏ / PᴀʏPᴀʟ
 
 Oʀ Dᴏɴᴀᴛᴇ: Mᴇssᴀɢᴇ Mᴇ @Mr_Tamil_KiD </b>
"""

    DEV_TXT = """
**__<u>Sᴩᴇᴄɪᴀʟ Tʜᴀɴᴋꜱ & Dᴇᴠᴇʟᴏᴩᴇʀꜱ</u>__

» 𝗦𝗢𝗨𝗥𝗖𝗘 𝗖𝗢𝗗𝗘 : [Click Here](https://github.com/MrTamilKiD) 

• [𝖬𝗋.𝖳𝖺𝗆𝗂𝗅_𝖪𝗂𝖣](https://github.com/MrTamilKiD) • 𝖬𝖺𝗂𝗇 𝖣𝖾𝗏
• @DalinkSupport • 𝖲𝗎𝖻 𝖣𝖾𝗏

⍟ Nᴇᴛᴡᴏʀᴋ - @Tamil_Network**
    """
    
    ADN_COMS = """
<b> Aᴅᴍɪɴ Cᴏᴍᴍᴀɴᴅs

ban 
unban 
log 
broadcast 
stats
</b>
"""

MYPLAN_TXT = """
╭────[ ʏᴏᴜʀ ᴘʟᴀɴ ᴅᴇᴀᴛᴀɪʟs ]────⍟
│
├👤 ᴜsᴇʀ: 
│
├🆔 ᴜsᴇʀɪᴅ: 
│
├🏷️ ᴘʟᴀɴ: {plan}
│
├💳 ʀᴇᴍᴀɪɴ: {paid_duration}
│
├✅ ᴘʟᴀɴ sᴛᴀʀᴛᴇᴅ ᴏɴ: {paid_on}
│
├🎯 ᴘʟᴀɴ ᴇɴᴅs ᴏɴ: {will_expire}
│
├📆 ᴅᴀᴛᴇ : 
│
├📑 ᴘʟᴀɴ ᴅɪsᴄʀɪᴘᴛɪᴏɴ:
│
╰───────────────────⍟
"""

########################## BUTTONS TXT ########################## 

class BUTTON(object):
    
    START_BUTTON = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('♡︎ 𝖣𝖾𝗏𝖾𝗅𝗈𝗉𝖾𝗋 🧑‍💻 ♡︎', url=f'http://t.me/mrtamilkid')
        ],[
        InlineKeyboardButton('📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌', url='https://t.me/kr_botz'),
        InlineKeyboardButton('⚡ 𝖲𝗎𝗉𝗉𝗈𝗋𝗍', url='https://t.me/HelpSXGroup')
        ],[
        InlineKeyboardButton('🦋 𝖱𝖾𝗊𝗎𝖾𝗌𝗍 🦋', url=f'http://t.me/kr_admin_bot')
        ],[
        InlineKeyboardButton('⚙️ 𝖧𝖾𝗅𝗉', callback_data='help'),
        InlineKeyboardButton('📚 𝖠𝖻𝗈𝗎𝗍', callback_data='about')
        ]]
    )

    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('⤬ ʀᴇᴏ̨ᴜᴇsᴛ ᴀ ᴡᴇʙsɪᴛᴇ ᴛᴏ ʙʏᴘᴀss ⤬', url=f'http://t.me/kr_admin_bot')
        ],[
        InlineKeyboardButton('📢 Uᴘᴅᴀᴛᴇs ', url=f"https://t.me/kr_botz"),
        InlineKeyboardButton('🗣️ Sᴜᴘᴘᴏʀᴛ', url=f"https://t.me/HelpSXGroup")
        ],[
        InlineKeyboardButton('⊛ ᴘʀᴇᴍɪᴜᴍ ᴘʟᴀɴs ⊛', callback_data="upgrade")
        ],[
        InlineKeyboardButton('⚙️ Hᴇʟᴘ', callback_data='help'),
        InlineKeyboardButton('📚 Aʙᴏᴜᴛ', callback_data='about')
        ]]
    )
    
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("💸 𝖣𝗈𝗇𝖺𝗍𝖾", callback_data="don")
        ],[
        InlineKeyboardButton("⛺ 𝖧𝗈𝗆𝖾", callback_data="home"),
        InlineKeyboardButton("Cʟᴏsᴇ ✘", callback_data="close")
        ]]
    )

    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton(' 𝖣𝗈𝗇𝖺𝗍𝖾 💸 𝖬𝖾 ', callback_data='don')
        ],[
        InlineKeyboardButton("📢 𝖴𝗉𝖽𝖺𝗍𝖾𝗌", url= "https://t.me/KR_Botz"),
        InlineKeyboardButton("👨‍💻 𝖣𝖾𝗏𝗌 🥷", callback_data = "dev")
        ],[
        InlineKeyboardButton("⛺ 𝖧𝗈𝗆𝖾", callback_data = "home"),
        InlineKeyboardButton("Cʟᴏsᴇ ✘", callback_data = "close")
        ]]
    )

    DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton("Pᴀʏ 💰 Aᴍᴏᴜɴᴛ",
                                             url="https://t.me/mr_tamil_kid")
        ],[
        InlineKeyboardButton("⛺ 𝖧𝗈𝗆𝖾", callback_data="home"),
        InlineKeyboardButton("Cʟᴏsᴇ ✘", callback_data="close")
        ]]
    ) 

    DEV_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton('Tค๓เl ᠰ KɪD 🇮🇳 ', url='https://t.me/Mr_Tamil_KiD'),
        ],[
        InlineKeyboardButton("≺≺ Bᴀᴄᴋ", callback_data = "about"),
        InlineKeyboardButton("Cʟᴏsᴇ ✗", callback_data = "close")
        ]]
    ) 

    ADN_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("Cʟᴏsᴇ ✗", callback_data = "close")
        ]]
    ) 
    
    PAID_JOIN_BUTTONS = InlineKeyboardMarkup( 
        [[
        InlineKeyboardButton("ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ", url='https://t.me/Paid_work_bot') 
        ],[
        InlineKeyboardButton("✗ Cʟᴏsᴇ", callback_data = "close")
        ]]
    ) 




