from .depositcashrequest import DepositCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from .widrawcashrequest import WidrawCashRequest

from ..commands import DepositCashCommand, PurchaseSecurityCommand, SellSecurityCommand, WidrawCashCommand

from datetime import datetime
from typing import Any

def CreateRequest(
        accountActivityType:str,
        accountId : str,
        netAmount : float,
        externalTransactionId : str,
        transactionDate: datetime,
        description : str,
        newBalance : float,
        settlementDate : datetime,
        securityId : str,
        quantity : int,
        unitPrice : float,
        fees : float) -> Any:


        match accountActivityType:
            case "R":
                request : DepositCashRequest = DepositCashRequest(
                    accountId = accountId,
                    externalTransactionId = externalTransactionId,
                    transactionDate = transactionDate,
                    netAmount = netAmount,
                    description = description,
                    newBalance = newBalance,
                    settlementDate = settlementDate)

                command : DepositCashCommand = DepositCashCommand()
                command.externalAccountId = request.accountId
                command.externalId = request.externalTransactionId
                command.date = request.transactionDate
                command.netAmount = request.netAmount
                command.description = request.description
                command.newBalance = request.newBalance
                command.settlementDate = request.settlementDate
                return command

            case "B":
                request : PurchaseSecurityRequest = PurchaseSecurityRequest(
                    accountId = accountId,
                    externalTransactionId = str(externalTransactionId),
                    transactionDate = transactionDate,
                    netAmount = netAmount,
                    description = description,
                    newBalance = newBalance,
                    settlementDate = settlementDate,
                    securityId = securityId,
                    unitPrice = unitPrice,
                    fees = fees,
                    quantity = quantity
                )
                
                command : PurchaseSecurityCommand = PurchaseSecurityCommand()
                command.externalAccountId = request.accountId
                command.externalId = request.externalTransactionId
                command.date = request.transactionDate
                command.netAmount = request.netAmount
                command.description = request.description
                command.newBalance = request.newBalance
                command.settlementDate = request.settlementDate
                command.securityId = request.securityId
                command.unitPrice = request.unitPrice
                command.fees = request.fees
                command.quantity = request.quantity

                return command

            case "S":

                request : SellSecurityRequest = SellSecurityRequest(
                    accountId = accountId,
                    externalTransactionId = str(externalTransactionId),
                    transactionDate = transactionDate,
                    netAmount = netAmount,
                    description = description,
                    newBalance = newBalance,
                    settlementDate = settlementDate,
                    securityId = securityId,
                    unitPrice = unitPrice,
                    fees = fees,
                    quantity = quantity
                )

                # command : SellSecurityCommand = SellSecurityCommand(
                #     accountId = request.accountId,
                #     externalTransactionId = request.externalTransactionId,
                #     transactionDate = request.transactionDate,
                #     netAmount = request.netAmount,
                #     description = request.description,
                #     newBalance = request.newBalance,
                #     settlementDate = request.settlementDate,
                #     securityId = request.securityId,
                #     unitPrice = request.unitPrice,
                #     fees = request.fees,
                #     quantity = request.quantity
                # )
                
                command : SellSecurityCommand = SellSecurityCommand()
                command.externalAccountId = request.accountId
                command.externalId = request.externalTransactionId
                command.date = request.transactionDate
                command.netAmount = request.netAmount
                command.description = request.description
                command.newBalance = request.newBalance
                command.settlementDate = request.settlementDate
                command.securityId = request.securityId
                command.unitPrice = request.unitPrice
                command.fees = request.fees
                command.quantity = request.quantity

                return command

            case "W":
                request : WidrawCashRequest = WidrawCashRequest(
                    accountId = accountId,
                    externalTransactionId = externalTransactionId,
                    transactionDate = transactionDate,
                    netAmount = netAmount,
                    description = description,
                    newBalance = newBalance,
                    settlementDate = settlementDate
                )
                
                # command: WidrawCashCommand = WidrawCashCommand(
                #     accountId = request.accountId,
                #     externalTransactionId = request.externalTransactionId,
                #     transactionDate = request.transactionDate,
                #     netAmount = request.netAmount,
                #     description = request.description,
                #     newBalance = request.newBalance,
                #     settlementDate = request.settlementDate
                # )

                command: WidrawCashCommand = WidrawCashCommand()              
                command.externalAccountId = request.accountId
                command.externalId = request.externalTransactionId
                command.date = request.transactionDate
                command.netAmount = request.netAmount
                command.description = request.description
                command.newBalance = request.newBalance
                command.settlementDate = request.settlementDate

                return command

            case _:
                raise Exception("Unknown account activity")