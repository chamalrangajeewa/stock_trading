from dependency_injector import containers, providers

from .service import databaseService

class Container(containers.DeclarativeContainer):

    database = providers.Factory(
        databaseService
    )