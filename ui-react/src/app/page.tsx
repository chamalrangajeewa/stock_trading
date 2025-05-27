'use client';

import  React, { Suspense } from "react";
import { useState, useEffect, useReducer} from "react";
import { AccountSnapshot } from "./accountSnapshot";
import AccountSnapshotComponent from "./component/accountsnapshot";
import { LoadingComponent } from "./component/loading";
import { accountReducer } from "./reducers/accountReducer"
import { StockSplitEvent } from "./reducers/stockSplitEvent";
import { ModifyAccountAllocationAmountEvent } from "./reducers/modifyAccountAllocationAmountEvent";
import { ModifySectorAllocationPercentageEvent } from "./reducers/modifySectorAllocationPercentageEvent";
import { ModifySecurityAllocationPercentageEvent } from "./reducers/modifySecurityAllocationPercentageEvent";
import useSWR from "swr";
import { AccountService } from "./service/accountService";
import { AccountSnapshotViewModel } from "./component/accountSnapshotViewModel";

function hydradeCalculatedValues(account : AccountSnapshot) : AccountSnapshot | null
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

  const { isLoading, error, data: portfolio} = useSWR("cacheKey", async (id) => {
      let service : AccountService  = new AccountService();
      let resposeData = await service.get(id);  
      let accountViewModel = new AccountSnapshotViewModel(resposeData);
      accountViewModel.reevaluateCalculatedFeilds();
      return accountViewModel;
    });

  return (
    <>
      
      
      <div className="p-4 overflow-auto">
        {/* {JSON.stringify(account)} */}
        {/* {process.env.NODE_ENV} */}
        <Suspense fallback={<LoadingComponent />}>
          {portfolio ? <AccountSnapshotComponent account={portfolio} /> : null}
        </Suspense>        
      </div>   
    </>  
  );
}
