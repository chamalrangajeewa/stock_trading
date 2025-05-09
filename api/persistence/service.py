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

    def __repr__(self):
        return f"<Account(id={self.id}, " \
               f"externalId=\"{self.externalId})>"

class SectorEntity(Base):

    __tablename__ = "sector"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    name = Column(String(100), name="name")
    fundAllocationPercentage = Column(Integer, name="fund_allocation_percentage", nullable=True, default=0)
    
    securities: Mapped[List["SecurityEntity"]] = relationship(back_populates="sector")

    def __repr__(self):
        return f"<Sector(id={self.id}, " \
               f"name=\"{self.name})>"
    
class SecurityEntity(Base):

    __tablename__ = "security"

    id = Column(String(50), primary_key=True, name="id")
    name = Column(String(100), name="name")
    sectorId = mapped_column(ForeignKey("sector.id"), type_= Integer )

    sector: Mapped[SectorEntity] = relationship(back_populates="securities")
    transactions: Mapped[List["TransactionEntity"]] = relationship(back_populates="security")

    def __repr__(self):
        return f"<Security(id={self.id}, " \
               f"name=\"{self.name})>"
    
   
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
    securityId = mapped_column(ForeignKey("security.id"), name ="security_id",  nullable=False)
    accountId = mapped_column(ForeignKey("account.id"), name="account_id", nullable=False)
    
    quantity = Column(Integer, name="quantity")
    livePerUnitCost = Column(Float, name="live_per_unit_cost")   
    averagePerUnitCost = Column(Float, name="average_per_unit_cost")

    totalPurchaseCost = Column(Float, name="total_purchase_cost")
    totalPurchaseFees = Column(Float, name="total_purchase_fees")

    totalSaleIncome = Column(Float, name="total_sales_income")
    totalSaleFees = Column(Float, name="total_sale_fees")
    totalRealisedProfit = Column(Float, name="total_realised_profit")

    fundAllocationPercentage = Column(Integer, name="fund_allocation_percentage", nullable=True, default=0)
    
    def __repr__(self):
        return f"<SecuritySnapShotEntity(id={self.id}, " \
               f"securityId=\"{self.securityId})>"
    
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

    security: Mapped[SecurityEntity] = relationship(back_populates="transactions")

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

class databaseService:
    async def process(self) -> str:
        return "saved"
    

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