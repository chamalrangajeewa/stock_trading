"""Containers module."""
from typing import List
from mediatr import Mediator
from .persistence import PersistenceContainer 
from .commands import CommandContainer, DepositCashCommandHandler, PurchaseSecurityCommandHandler, SellSecurityCommandHandler,WidrawCashCommandHandler, ViewDashboardCashCommand, ViewDashboardCommandHandler
from .routers.containers import RouteContainer

from dependency_injector import containers, providers

def get_initialised_mediator(mediatorInstance: Mediator, handlerCollection : List) -> Mediator:
    
    for x in handlerCollection:
        hanlder, y = x
        mediatorInstance.handler(hanlder)

    return mediatorInstance

def create_Handler(HandlerCls:type, is_behavior:bool = False):
        print(HandlerCls.__class__)
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

    # persistence_package.container.wire(modules=[".routers.transactions"])
    persistence_package.container.wire(modules=[".routers.transactions",".routers.account"])

    command_package = providers.Container(
        CommandContainer,
        storage_client = persistence_package.container.database_sqllite
    )

    # command_package.container.wire(modules=[".routers.transactions"])
    command_package.container.wire(modules=[".routers.transactions",".routers.account"])

    route_package = providers.Container(
        RouteContainer
    )

    # route_package.container.wire(modules=[".routers.transactions"])
    route_package.container.wire(modules=[".routers.transactions",".routers.account"])

    __handlertype_handlerFactory_pair = [(DepositCashCommandHandler, command_package.container.depositcashcommand_handler),
         (PurchaseSecurityCommandHandler, command_package.container.purchasesecuritycommand_handler),
         (SellSecurityCommandHandler, command_package.container.sellsecuritycommand_handler),
         (WidrawCashCommandHandler, command_package.container.widrawcashcommand_handler),
         (ViewDashboardCommandHandler, command_package.container.viewdashboardcommand_handler)]
    
    collection =  providers.Object(__handlertype_handlerFactory_pair)

    __mediator = providers.Factory(Mediator, handler_class_manager = create_Handler)   
    mediator = providers.Factory(get_initialised_mediator, mediatorInstance = __mediator, handlerCollection = collection)