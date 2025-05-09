from .depositcashrequest import DepositCashRequest
from .purchasesecurityrequest import PurchaseSecurityRequest
from .sellsecurityrequest import SellSecurityRequest
from .widrawcashrequest import WidrawCashRequest

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
                command : DepositCashRequest = DepositCashRequest()
                command.accountId = accountId
                command.externalTransactionId = externalTransactionId
                command.transactionDate = transactionDate
                command.netAmount = netAmount
                command.description = description
                command.newBalance = newBalance
                command.settlementDate = settlementDate
                return command

            case "B":
                command : PurchaseSecurityRequest = PurchaseSecurityRequest()
                command.accountId = accountId
                command.externalTransactionId = externalTransactionId
                command.transactionDate = transactionDate
                command.netAmount = netAmount
                command.description = description
                command.newBalance = newBalance
                command.settlementDate = settlementDate
                command.securityId = securityId
                command.unitPrice = unitPrice
                command.fees = fees
                command.quantity = quantity
                return command

            case "S":

                command : SellSecurityRequest = SellSecurityRequest()
                command.accountId = accountId
                command.externalTransactionId = externalTransactionId
                command.transactionDate = transactionDate
                command.netAmount = netAmount
                command.description = description
                command.newBalance = newBalance
                command.settlementDate = settlementDate
                command.securityId = securityId
                command.unitPrice = unitPrice
                command.fees = fees
                command.quantity = quantity
                return command

            case "W":
                command : WidrawCashRequest = WidrawCashRequest()
                command.accountId = accountId
                command.externalTransactionId = externalTransactionId
                command.transactionDate = transactionDate
                command.netAmount = netAmount
                command.description = description
                command.newBalance = newBalance
                command.settlementDate = settlementDate
                return command

            case _:
                raise Exception("Unknown account activity")