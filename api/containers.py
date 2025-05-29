"""Containers module."""
from typing import List
from mediatr import Mediator
from .persistence import PersistenceContainer 
from .commands import AdjustAccountAllocationAmountCommandHandler, AdjustSectorAllocationPercentageCommandHandler, AdjustSecurityAllocationPercentageCommandHandler, CommandContainer, DepositCashCommandHandler, PurchaseSecurityCommandHandler, SellSecurityCommandHandler, StocksplitCommandHandler,WidrawCashCommandHandler, ViewDashboardCommandHandler, SyncLivePriceCommandHandler
from .routers.containers import RouteContainer

from dependency_injector import containers, providers

def get_initialised_mediator(mediatorInstance: Mediator, handlerCollection : List) -> Mediator:
    
    for x in handlerCollection:
        hanlder, y = x
        mediatorInstance.handler(hanlder)

    return mediatorInstance

def create_Handler(HandlerCls:type, is_behavior:bool = False):
        for x in ApplicationContainer.collection():
            hanlder, y = x
            if hanlder == HandlerCls:
                 return y()
 
class ApplicationContainer(containers.DeclarativeContainer):

    wiring_config = containers.WiringConfiguration(modules=[".routers.transactions",".routers.account"])
    config = providers.Configuration(strict=True)

    persistence_package = providers.Container(
        PersistenceContainer,
        config = config
    )

    persistence_package.container.wire(modules=[".routers.transactions"])
    
    command_package = providers.Container(
        CommandContainer,
        storage_client = persistence_package.container.database_sqllite
    )

    command_package.container.wire(modules=[".routers.transactions"])
    
    route_package = providers.Container(
        RouteContainer
    )

    route_package.container.wire(modules=[".routers.transactions"])
   
    __handlertype_handlerFactory_pair = [
         (StocksplitCommandHandler, command_package.container.stocksplitcommand_handler),
         (AdjustSecurityAllocationPercentageCommandHandler, command_package.container.adjustsecurityallocationpercentagecommand_handler),
         (AdjustSectorAllocationPercentageCommandHandler, command_package.container.adjustsectorallocationpercentagecommand_handler),
         (AdjustAccountAllocationAmountCommandHandler, command_package.container.adjustaccountallocationamountcommand_handler),
         (DepositCashCommandHandler, command_package.container.depositcashcommand_handler),
         (PurchaseSecurityCommandHandler, command_package.container.purchasesecuritycommand_handler),
         (SellSecurityCommandHandler, command_package.container.sellsecuritycommand_handler),
         (WidrawCashCommandHandler, command_package.container.widrawcashcommand_handler),
         (ViewDashboardCommandHandler, command_package.container.viewdashboardcommand_handler),
         (SyncLivePriceCommandHandler, command_package.container.synclivepricecommand_handler)]
    
    collection =  providers.Object(__handlertype_handlerFactory_pair)

    __mediator = providers.Factory(Mediator, handler_class_manager = create_Handler)   
    mediator = providers.Factory(get_initialised_mediator, mediatorInstance = __mediator, handlerCollection = collection)