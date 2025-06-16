from datetime import datetime
from ..persistence.database import Database
from ..persistence.service import SecurityEntity
from sqlalchemy.orm import Session
from pydantic import BaseModel
from bs4 import BeautifulSoup
import aiohttp
import asyncio
from playwright.async_api import async_playwright

class SyncLivePriceCommand(BaseModel):
   securityId : str
   date : datetime
   unitPrice : float

class SyncLivePriceCommandHandler():
    
   def __init__(self, storageClient : Database):
       self._storageClient = storageClient       

   async def handle(self, request: SyncLivePriceCommand) -> str:
       
      async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("https://playwright.dev")
        print(await page.title())
        await browser.close()

    #   async with aiohttp.ClientSession() as session:
    #     async with session.get('https://www.cse.lk/pages/company-profile/company-profile.component.html?symbol=HNB.N0000') as resp:
    #         print(resp.status)
    #         html_doc = await resp.text()
    #         soup = BeautifulSoup(html_doc, 'html.parser')
    #         print(soup.prettify())
    #         element = soup.find("div", class_="last-trade-price").text
    #         print(element)

      return "OK"