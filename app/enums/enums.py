from enum import Enum
from dataclasses import dataclass

@dataclass
class CommandsTexts(Enum):
    GAME_RULES: str
    SUPPORT: str

class CommandsTextsRU(CommandsTexts):
    GAME_RULES = ""
    SUPPORT = "По техническим и др. вопросам пишите админу:\n@doomer_pavel"

class CommandsTextsUA(CommandsTexts):
    GAME_RULES = ""
    SUPPORT = "З технічних та інших питань пишіть адміністратору:\n@doomer_pavel"

class CommandsTextsEN(CommandsTexts):
    GAME_RULES = ""
    SUPPORT = "For technical and other inquiries, please contact the admin:\n@doomer_pavel"
