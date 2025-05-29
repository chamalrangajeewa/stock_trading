from datetime import datetime
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import selectinload, joinedload,subqueryload

from ..persistence.database import Database
from ..persistence.service import AccountEntity, SectorSnapShotEntity, SecurityEntity, SecuritySnapShotEntity, TransactionEntity

from typing import List
from pydantic import BaseModel

class SecuritySnapshot(BaseModel):

    name : str
    id : str    
    allocationPercentage: float
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float
    quantity : float
    averagePerUnitCost : float
    livePerUnitCost : float


class SectorSnapshot(BaseModel):

    name : str
    securities : List[SecuritySnapshot] = list()
    allocationPercentage: float
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float


class AccountSnapshot(BaseModel):
    
    id : str
    owner : str
    allocationAmount : float
    balanceAmount : float
    netCost : float
    marketValue : float
    saleFee : float
    netProceeds : float
    gains: float
    gainsPerncetage:float
    sectors : List[SectorSnapshot] = list()

class ViewDashboardCashCommand:
  
   externalAccountId : str
   

class ViewDashboardCommandHandler():

    def __init__(self, storageClient : Database):
       self._storageClient = storageClient          

    async def handle(self, request: ViewDashboardCashCommand) -> AccountSnapshot:
       with self._storageClient.session() as _session:
            session : Session = _session

            accountEntityQuery = select(AccountEntity).options(
                joinedload(AccountEntity.sectorSnapshots).joinedload(
                    SectorSnapShotEntity.securitySnapshots).joinedload(SecuritySnapShotEntity.security)
                ).where(AccountEntity.externalId == request.externalAccountId)
            
            print(accountEntityQuery)

            accountEntity = session.execute(accountEntityQuery).first()
            
            if not accountEntity:
                raise Exception("account not found")
        
            sectors:List[SectorSnapshot] = list()
            
            for sectorSnapshotEntity in accountEntity._t[0].sectorSnapshots:
                
                if len(sectorSnapshotEntity.securitySnapshots) == 0:
                    continue

                sectorEntity = sectorSnapshotEntity.sector                

                securities:List[SecuritySnapshot] = list()

                for securitysnapshot in sectorSnapshotEntity.securitySnapshots:
                    
                    if securitysnapshot.quantity == 0:
                        continue

                    security:SecuritySnapshot =  SecuritySnapshot(
                        allocationPercentage = securitysnapshot.fundAllocationPercentage,
                        averagePerUnitCost= securitysnapshot.averagePerUnitCost,
                        livePerUnitCost= securitysnapshot.security.livePerUnitCost,
                        quantity = securitysnapshot.quantity,
                        allocationAmount=0,
                        balanceAmount=0,
                        gains=0,
                        gainsPerncetage=0,
                        marketValue=0,
                        netCost=0,
                        saleFee=0,
                        netProceeds=0,
                        id=securitysnapshot.securityId,
                        name=securitysnapshot.security.name)
                    
                    securities.append(security)
                    
                sector:SectorSnapshot = SectorSnapshot(
                    name = sectorEntity.name,
                    allocationPercentage = sectorSnapshotEntity.fundAllocationPercentage,
                    allocationAmount=0,
                    balanceAmount=0,
                    gains=0,
                    gainsPerncetage=0,
                    marketValue=0,
                    netCost=0,
                    netProceeds=0,
                    saleFee=0,
                    securities= securities                                   
                )

                sectors.append(sector)
                

            result: AccountSnapshot = AccountSnapshot(
                id = accountEntity._t[0].externalId,
                allocationAmount = accountEntity._t[0].investment,
                balanceAmount=accountEntity._t[0].fundBalance,
                gains=0,
                gainsPerncetage=0,
                marketValue=0,
                netCost=0,
                netProceeds=0,
                owner="chaaml",
                saleFee=0,
                sectors= sectors            
                )
            
            return result