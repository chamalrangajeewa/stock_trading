"""Models module."""

from typing import List
from sqlalchemy import Column, ForeignKey, String, Float, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .database import Base

class AccountEntity(Base):

    __tablename__ = "account"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    externalId = Column(String(100), index=True, unique=True,  name="externalId")   
    fundBalance = Column(Float, name="fund_balance")
    investment = Column(Float, name="investment")

    def __repr__(self):
        return f"<Account(id={self.id}, " \
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
    sectorId = mapped_column(ForeignKey("sector.id"))

    sector: Mapped[SectorEntity] = relationship(back_populates="securities")
    transactions: Mapped[List["TransactionEntity"]] = relationship(back_populates="security")

    def __repr__(self):
        return f"<Security(id={self.id}, " \
               f"name=\"{self.name})>"
    
   
class SecuritySnapShotEntity(Base):

    __tablename__ = "securitysnapshot"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    securityId = mapped_column(ForeignKey("security.id"))
    accountId = mapped_column(ForeignKey("account.id"))
    totalQuantity = Column(Integer, name="total_quantity")
    currentPerUnitCost = Column(Float, name="current_per_unit_cost")
    averagePerUnitCost = Column(Float, name="average_per_unit_cost")
    totalPurchaseCost = Column(Float, name="total_purchase_cost")
    totalPurchaseCommission = Column(Float, name="total_purchase_commission")  
    totalSaleIncome = Column(Float, name="total_income")
    totalSaleCommission = Column(Float, name="total_sale_commission")
    totalRealisedProfit = Column(Float, name="total_realised_profit")


    def __repr__(self):
        return f"<SecuritySnapShotEntity(id={self.id}, " \
               f"securityId=\"{self.securityId})>"
    

class TransactionEntity(Base):

    __tablename__ = "transaction"

    id = Column(Integer, primary_key=True, autoincrement=True, name="id")
    date = Column(DateTime, name="date")
    type = Column(String(50), name="type")
    externalId = Column(String(50), unique=True, name="external_id")
    description= Column(String(500), name="description")
    perUnitCost = Column(Float, name="per_unit_cost", nullable=True , default=0)
    quantity = Column(Integer, name="quantity", nullable=True, default = 0)
    amount = Column(Float, name="amount")
    commission = Column(Float, name="commission", nullable=True)
    balance = Column(Float, name="balance")
    settlementDate = Column(DateTime, name="settlement_date")
    securityId = mapped_column(ForeignKey("security.id"), name="security_id", nullable=True)
    accountId = mapped_column(ForeignKey("account.id"), name="account_id")

    security: Mapped[SecurityEntity] = relationship(back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, " \
               f"date=\"{self.date}\", " \
               f"externalId=\"{self.externalId}\", " \
               f"perUnitCost=\"{self.perUnitCost}\", " \
               f"quantity=\"{self.quantity}\", " \
               f"securityId=\"{self.securityId}\", " \
               f"type={self.type})>"

class databaseService:
    async def process(self) -> str:
        return "saved"