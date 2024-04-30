from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    amqp_url: str
    test_build: bool
    postgres_url: str
    keycloak_url: str
    keycloak_realm: str
    keycloak_secret: str
    keycloak_id: str
    model_config = SettingsConfigDict(env_file='.env')


input_data = {
    'amqp_url': 'amqp://guest:guest@localhost:5672/',
    'test_build': True,
    'postgres_url': 'postgresql://postgres:postgres@db:5432/postgres',
    'keycloak_url': 'http://keycloak:8080/realms',
    'keycloak_realm': 'Keycloak',
    'keycloak_secret': 'Gjlv8tTjZaefrYajXNrjUlVvmscdWz9X',
    'keycloak_id': 'Alex'
}
try:

    settings = Settings(**input_data)

except Exception as e:
    print(f"An error occurred: {e}")