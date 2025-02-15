from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_DIALECT: str = "postgresql"
    DB_DRIVER: str = "psycopg2"
    DB_NAME: str = "pill_keeper_local_db"
    DB_USER: str = "postgres"
    DB_PASSWORD: str = "password"
    DB_HOST: str = "127.0.0.1"
    DB_PORT: str = "5432"

    @property
    def get_db_url(self):
        return f"{self.DB_DIALECT}+{self.DB_DRIVER}://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings(
    _env_file_encoding="utf-8",
)
