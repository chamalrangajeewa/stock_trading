from dependency_injector import containers, providers
from .depositcashcommandhandler import DepositCashCommandHandler
from .purchasesecuritycommandhandler import PurchaseSecurityCommandHandler
from .sellsecuritycommandhandler import SellSecurityCommandHandler
from .widrawcashcommandhandler import WidrawCashCommandHandler
from .viewdashboardcommandhandler import ViewDashboardCommandHandler
    
class Container(containers.DeclarativeContainer):

    storage_client = providers.Dependency()

    depositcashcommand_handler = providers.Factory(
        DepositCashCommandHandler,
        storageClient = storage_client 
    )

    purchasesecuritycommand_handler = providers.Factory(
        PurchaseSecurityCommandHandler,
        storageClient = storage_client 
    )

    sellsecuritycommand_handler = providers.Factory(
        SellSecurityCommandHandler,
        storageClient = storage_client 
    )

    widrawcashcommand_handler = providers.Factory(
        WidrawCashCommandHandler,
        storageClient = storage_client 
    )

    viewdashboardcommand_handler = providers.Factory(
        ViewDashboardCommandHandler,
        storageClient = storage_client 
    )