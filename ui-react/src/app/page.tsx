'use client';

import  React from "react";
import { useState, useEffect } from "react";
import { AccountSnapshot } from "./accountSnapshot";
import AccountSnapshotComponent from "./component/accountsnapshot";

function hydradeCalculatedValues(account : AccountSnapshot)
{
      if (!account) {
        return null
      }

      for (let index = 0; index < account.sectors.length; index++) {
          const sector = account.sectors[index];
          sector.allocationAmount = account.allocationAmount * sector.allocationPercentage * 0.01;
      
          for (let i = 0; i < sector.securities.length; i++) {
            const security = sector.securities[i];

            security.allocationAmount = sector.allocationAmount * security.allocationPercentage * 0.01;
            security.netCost = security.averagePerUnitCost * security.quantity;
            security.marketValue = security.livePerUnitCost * security.quantity;
            security.balanceAmount = security.allocationAmount - security.netCost;
            security.saleFee = security.marketValue * 0.0112;
            security.netProceeds = security.marketValue - security.saleFee;
            security.gains = security.marketValue - security.saleFee - security.netCost;
            security.gainsPerncetage = (security.gains / security.netCost) * 100;        
          }

          sector.marketValue = sector.securities.map(o => o.marketValue).reduce((a,b) => a + b, 0);
          sector.saleFee = sector.securities.map(o => o.saleFee).reduce((a,b) => a + b, 0);
          sector.netCost = sector.securities.map(o => o.netCost).reduce((a,b) => a + b, 0);
          sector.netProceeds = sector.securities.map(o => o.netProceeds).reduce((a,b) => a + b, 0);
          sector.gains = sector.securities.map(o => o.gains).reduce((a,b) => a + b, 0);
          sector.gainsPerncetage = (sector.gains / sector.netCost) * 100; 
          sector.balanceAmount = sector.allocationAmount - sector.netCost;
        }

          account.marketValue = account.sectors.map(o => o.marketValue).reduce((a,b) => a + b, 0);
          account.saleFee = account.sectors.map(o => o.saleFee).reduce((a,b) => a + b, 0);
          account.netCost = account.sectors.map(o => o.netCost).reduce((a,b) => a + b, 0);
          account.netProceeds = account.sectors.map(o => o.netProceeds).reduce((a,b) => a + b, 0);
          account.gains = account.sectors.map(o => o.gains).reduce((a,b) => a + b, 0);
          account.gainsPerncetage = (account.gains / account.netCost) * 100; 
          account.balanceAmount = account.balanceAmount;

          return account;
}


export default function Home() {

  const [portfolio, setPortfolio] = useState(null);

  useEffect(() => {

    let ignore = false;

    async function fetchPortfolio() {
      // const respose = await fetch("https://682383c365ba05803397073e.mockapi.io/api/cse/Account")
      const respose = await fetch("http://127.0.0.1:8000/account/dashboard")
      debugger;
      if(!respose.ok)
        throw new Error("error loading");  

      const account : AccountSnapshot  = await respose.json();

      debugger
      if(!ignore){
          const accountAfterSumming : any = hydradeCalculatedValues(account);
          setPortfolio(accountAfterSumming);
      }
        
    }

    fetchPortfolio();

    return () => {
      ignore = true;
    }
  }, []);


  return (
    <>
      <div className="p-4 overflow-auto">
        {/* <div>shkshfskh</div>
        <div>{JSON.stringify(portfolio)}</div> */}
        {/* <AccountSnapshotComponent account1 = { portfolio }></AccountSnapshotComponent> */}
        {portfolio ? <AccountSnapshotComponent account1={portfolio} /> : null}
      </div>   
    </>  
  );
}
