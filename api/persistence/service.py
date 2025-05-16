"""Models module."""

from typing import List
from sqlalchemy import Column, ForeignKey, String, Float, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base

class AccountEntity(Base):

    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    externalId = Column(String(100), index=True, unique=True,  name="external_id")   
    fundBalance = Column(Float, name="fund_balance")
    investment = Column(Float, name="investment")

    sectorSnapshots: Mapped[List["SectorSnapShotEntity"]] = relationship(back_populates="account")
    
    def __repr__(self):
        return f"<Account(id={self.id}, " \
               f"<fundBalance(id={self.fundBalance}, " \
               f"<investment(id={self.investment}, " \
               f"externalId=\"{self.externalId})>"

class SectorEntity(Base):

    __tablename__ = "sector"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    name = Column(String(100), name="name")
    
    securities: Mapped[List["SecurityEntity"]] = relationship(back_populates="sector")

    def __repr__(self):
        return f"<Sector(id={self.id}, " \
               f"name=\"{self.name})>"

class SecurityEntity(Base):

    __tablename__ = "security"

    id = Column(String(50), primary_key=True, name="id")
    name = Column(String(100), name="name")
    sectorId = mapped_column(ForeignKey("sector.id"), type_= Integer )
    livePerUnitCost = Column(Float, name="live_per_unit_cost", default=0, nullable=False)

    sector: Mapped[SectorEntity] = relationship(back_populates="securities")

    def __repr__(self):
        return f"<Security(id={self.id}, " \
               f"<name(id={self.name}, " \
               f"<sectorId(id={self.sectorId}, " \
               f"livePerUnitCost=\"{self.livePerUnitCost})>"  


class SectorSnapShotEntity(Base):

    __tablename__ = "sectorsnapshot"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    accountId = mapped_column(ForeignKey("account.id"), name="account_id", nullable=False)
    sectorId = mapped_column(ForeignKey("sector.id"), name="sector_id", nullable=False)
    fundAllocationPercentage = Column(Integer, name="fund_allocation_percentage", nullable=False, default=0)

    sector: Mapped[SectorEntity] = relationship()
    account: Mapped[AccountEntity] = relationship(back_populates="sectorSnapshots")

    securitySnapshots : Mapped[List["SecuritySnapShotEntity"]] = relationship(back_populates="sectorSnapshot")

    def __repr__(self):
        return f"<SectorSnapshot(id={self.id}, " \
               f"<accountId(id={self.accountId}, " \
               f"<sectorId(id={self.sectorId}, " \
               f"fundAllocationPercentage=\"{self.fundAllocationPercentage})>"

class SecuritySnapShotEntity(Base):

    def __init__(self) -> None:
        self.averagePerUnitCost = 0
        self.quantity = 0
        self.totalPurchaseCost = 0
        self.totalPurchaseFees = 0
        self.totalRealisedProfit = 0
        self.totalSaleFees = 0
        self.totalSaleIncome = 0
        
    __tablename__ = "securitysnapshot"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    sectorSnapshotId = mapped_column(ForeignKey("sectorsnapshot.id"), name ="sectorsnapshot_id",  nullable=False)
    securityId = mapped_column(ForeignKey("security.id"), name ="security_id",  nullable=False)
    # accountId = mapped_column(ForeignKey("account.id"), name="account_id", nullable=False)
    
    quantity = Column(Integer, name="quantity")   
    averagePerUnitCost = Column(Float, name="average_per_unit_cost")
    fundAllocationPercentage = Column(Integer, name="fund_allocation_percentage", nullable=False, default=0)
    
    totalPurchaseCost = Column(Float, name="total_purchase_cost")
    totalPurchaseFees = Column(Float, name="total_purchase_fees")

    totalSaleIncome = Column(Float, name="total_sales_income")
    totalSaleFees = Column(Float, name="total_sale_fees")
    totalRealisedProfit = Column(Float, name="total_realised_profit")
    
    sectorSnapshot: Mapped[SectorSnapShotEntity] = relationship(back_populates="securitySnapshots")

    # account: Mapped[AccountEntity] = relationship(back_populates="securitySnapshots")
    security: Mapped[SecurityEntity] = relationship()

    def __repr__(self):
        return f"<SecuritySnapShotEntity(id={self.id}, " \
               f"<quantity(id={self.quantity}, " \
               f"<securityId(id={self.securityId}, " \
               f"<averagePerUnitCost(id={self.averagePerUnitCost}, " \
               f"<fundAllocationPercentage(id={self.fundAllocationPercentage}, " \
               f"<totalPurchaseCost(id={self.totalPurchaseCost}, " \
               f"<totalPurchaseFees(id={self.totalPurchaseFees}, " \
               f"<totalSaleIncome(id={self.totalSaleIncome}, " \
               f"<totalSaleFees(id={self.totalSaleFees}, " \
               f"<totalRealisedProfit(id={self.totalRealisedProfit}, " \
               f"sectorSnapshotId=\"{self.sectorSnapshotId})>"
    
class TransactionEntity(Base):

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    externalId = Column(String(50), unique=True, name="external_id")
    accountId = mapped_column(ForeignKey("account.id"), name="account_id")
    date = Column(DateTime, name="date", nullable=False)
    type = Column(String(50), name="type", nullable=False) 
    description= Column(String(1000), name="description", nullable=True)   
    netAmount = Column(Float, name="net_amount", nullable=False) 
    newBalance = Column(Float, name="new_balance", nullable=False)
    settlementDate = Column(DateTime, name="settlement_date", nullable=False)
    fees = Column(Float, name="fees", nullable=True, default=0)
    
    securityId = mapped_column(ForeignKey("security.id"), name="security_id", nullable=True)  
    perUnitCost = Column(Float, name="per_unit_cost", nullable=True, default=0)
    quantity = Column(Integer, name="quantity", nullable=True, default = 0)

    security: Mapped[SecurityEntity] = relationship()

    def __repr__(self):
        return f"<Transaction(id={self.id}, " \
               f"externalId=\"{self.externalId}\", " \
               f"accountId=\"{self.accountId}\", " \
               f"date=\"{self.date}\", " \
               f"type=\"{self.type}\", " \
               f"description=\"{self.description}\", " \
               f"netAmount=\"{self.netAmount}\", " \
               f"newBalance=\"{self.newBalance}\", " \
               f"settlementDate=\"{self.settlementDate}\", " \
               f"perUnitCost=\"{self.perUnitCost}\", " \
               f"quantity=\"{self.quantity}\", " \
               f"securityId=\"{self.securityId}\", " \
               f"fees={self.fees})>"
    
class AccountActivityEntity(Base):

    __tablename__ = "account_activity"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    externalId = Column(String(50), unique=True, name="external_id")
    accountId = mapped_column(ForeignKey("account.id"), name="account_id")
    date = Column(DateTime, name="date", nullable=False)
    type = Column(String(50), name="type", nullable=False) 
    description= Column(String(1000), name="description", nullable=True)   
    netAmount = Column(Float, name="net_amount", nullable=False) 
    newBalance = Column(Float, name="new_balance", nullable=False)
    settlementDate = Column(DateTime, name="settlement_date", nullable=False)
    fees = Column(Float, name="fees", nullable=True, default=0)