from dependency_injector import containers, providers
from .viewdashboardcommandhandler import ViewDashboardCommandHandler
    
class Container(containers.DeclarativeContainer):

    storage_client = providers.Dependency()

    viewdashboardcommand_handler = providers.Factory(
        ViewDashboardCommandHandler,
        storageClient = storage_client 
    )

    