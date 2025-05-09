from typing import Any, Callable

from mediatr import Mediator

from api.commands import CommandContainer
from api.persistence import PersistenceContainer

from dependency_injector import containers, providers
    
class RouteContainer(containers.DeclarativeContainer):

    g = 1
    # wiring_config = containers.WiringConfiguration(modules=[".transactions"])

    # persistence_package = providers.Container(
    #     PersistenceContainer
    # )

    # persistence_package.container.wire(modules=[".transactions"])

    # command_package = providers.Container(
    #     CommandContainer,
    #     database = persistence_package.container.database
    # )

    # command_package.container.wire(modules=[".transactions"])
