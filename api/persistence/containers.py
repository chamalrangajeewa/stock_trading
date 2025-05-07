from dependency_injector import containers, providers

from .database import Database

from .service import databaseService

class Container(containers.DeclarativeContainer):

    config = providers.Configuration(strict=True)
    
    connection = providers.Factory(str, config.db.url)
    
    database_sqllite = providers.Factory(
        Database,
        connectionstring = "sqlite:///./webapp.db"
    )

    database = providers.Factory(
        databaseService
    )