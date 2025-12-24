from dataclasses import dataclass
from os import getenv

from dotenv import load_dotenv


@dataclass
class TgBot:
    bot_token: str

@dataclass
class DB:
    name: str
    user: str
    password: str
    port: int
    host: str

    def __post_init__(self):
        self.url = f"postgresql+asyncpg://{self.user}:{self.password}@{self.host}/{self.name}"

@dataclass
class Config:
    tg_bot: TgBot
    db: DB

def load_config() -> Config:
    load_dotenv(dotenv_path="../../../GeoGameBot_v1/.env")

    return Config(
        TgBot(
            getenv("BOT_TOKEN")
        ),
        DB(
            getenv("POSTGRES_NAME"),
            getenv("POSTGRES_USER"),
            getenv("POSTGRES_PASSWORD"),
            int(getenv("POSTGRES_PORT")),
            getenv("POSTGRES_HOST")
        )
    )


if __name__ == "__main__":
    print(load_config())
