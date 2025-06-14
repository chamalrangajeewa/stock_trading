from dependency_injector import containers, providers

from .synclivepricecommandhandler import SyncLivePriceCommandHandler
from .depositcashcommandhandler import DepositCashCommandHandler
from .purchasesecuritycommandhandler import PurchaseSecurityCommandHandler
from .sellsecuritycommandhandler import SellSecurityCommandHandler
from .widrawcashcommandhandler import WidrawCashCommandHandler
from .adjustaccountallocationamountcommandhandler import AdjustAccountAllocationAmountCommandHandler
from .adjustsectorallocationpercentagecommandhandler import AdjustSectorAllocationPercentageCommandHandler
from .adjustsecurityallocationpercentagecommandhandler import AdjustSecurityAllocationPercentageCommandHandler
from .stocksplitcommandhandler import StocksplitCommandHandler

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

    synclivepricecommand_handler = providers.Factory(
        SyncLivePriceCommandHandler,
        storageClient = storage_client 
    )

    adjustaccountallocationamountcommand_handler = providers.Factory(
        AdjustAccountAllocationAmountCommandHandler,
        storageClient = storage_client 
    )

    adjustsectorallocationpercentagecommand_handler = providers.Factory(
        AdjustSectorAllocationPercentageCommandHandler,
        storageClient = storage_client 
    )

    adjustsecurityallocationpercentagecommand_handler = providers.Factory(
        AdjustSecurityAllocationPercentageCommandHandler,
        storageClient = storage_client 
    )

    stocksplitcommand_handler = providers.Factory(
        StocksplitCommandHandler,
        storageClient = storage_client 
    )