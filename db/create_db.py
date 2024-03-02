from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Создание экземпляра движка SQLAlchemy
engine = create_engine("mysql+pymysql://root:@localhost/social_network")

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# Создание таблиц
Base.metadata.create_all(engine)

# Закрытие сессии
session.close()