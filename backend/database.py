import warnings
from sqlalchemy.exc import SAWarning
from sqlmodel import Session, create_engine
from sqlmodel.sql.expression import Select, SelectOfScalar
from config import config_local, dir_path

import models

warnings.filterwarnings("ignore", category=SAWarning)
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
engine = create_engine('sqlite:///{}/{}.db'.format(dir_path, config_local['database']['name']), echo=False)
models.SQLModel.metadata.create_all(engine)


def get_session():
    return Session(engine)
