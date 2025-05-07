from dependency_injector import containers, providers
from .depositcashcommandhandler import DepositCashCommandHandler
from .purchasesecuritycommandhandler import PurchaseSecurityCommandHandler
from .sellsecuritycommandhandler import SalesSecurityCommandHandler
from .widrawcashcommandhandler import WidrawCashCommandHandler
    
class Container(containers.DeclarativeContainer):

    database = providers.Dependency()
    storage_client = providers.Dependency()

    depositcashcommand_handler = providers.Factory(
        DepositCashCommandHandler,
        databaseService = database,
        storageClient = storage_client 
    )

    purchasesecuritycommand_handler = providers.Factory(
        PurchaseSecurityCommandHandler,
        databaseService = database 
    )

    salessecuritycommand_handler = providers.Factory(
        SalesSecurityCommandHandler,
        databaseService = database 
    )

    widrawcashcommand_handler = providers.Factory(
        WidrawCashCommandHandler,
        databaseService = database 
    )