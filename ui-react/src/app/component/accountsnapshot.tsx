'use client';

import { useReducer } from 'react';
import  React from "react";
import SectorSnapshotComponent from "./sectorsnapshot";
import SecuritySnapshotComponent from "./securitysnapshot";
import { accountReducer } from '../reducers/accountReducer';
import { StockSplitEvent } from '../reducers/stockSplitEvent';
import { ModifyAccountAllocationAmountEvent } from '../reducers/modifyAccountAllocationAmountEvent';
import { ModifySectorAllocationPercentageEvent } from '../reducers/modifySectorAllocationPercentageEvent';
import { ModifySecurityAllocationPercentageEvent } from '../reducers/modifySecurityAllocationPercentageEvent';
import { AccountSnapshotViewModel } from './accountSnapshotViewModel';
import useSWR from 'swr';
import { AccountService } from '../service/accountService';

export interface AccountProps {
  account: AccountSnapshotViewModel;
}

type AccountEvent = StockSplitEvent | 
ModifyAccountAllocationAmountEvent | 
ModifySectorAllocationPercentageEvent | 
ModifySecurityAllocationPercentageEvent;

export default function AccountSnapshotComponent(props: AccountProps) {
  
  const { isLoading, error, data: portfolio} = useSWR("cacheKey", async (id) => {
      let service : AccountService  = new AccountService();
      let resposeData = await service.get("CAS/104948-LI/0");
      let accountViewModel = new AccountSnapshotViewModel(resposeData);
      accountViewModel.reevaluateCalculatedFeilds();
      return accountViewModel;
    });

  const [account, dispatch] = useReducer(accountReducer, props.account);

  const handleAccountEvent = async (e:Event, action: AccountEvent) => {
    e.stopPropagation();
    
    let service : AccountService  = new AccountService();
    
    if (action instanceof ModifyAccountAllocationAmountEvent) {
      await service.modifyAccountInvestmentAllocationAmount({
        accountId: account.id, 
        allocationAmount : action.allocationAmount
      });  
    }

    if (action instanceof ModifySectorAllocationPercentageEvent) {
      await service.modifySectorAllocationPercentage({
        accountId:account.id, 
        name: action.name, 
        allocationPercentage:action.allocationPercentage
      });  
    }

    if (action instanceof ModifySecurityAllocationPercentageEvent) {
      await service.modifySecurityAllocationPercentage({
        accountId : account.id, 
        allocationPercentage: action.allocationPercentage, 
        securityId: action.securityId});  
    }

    if (action instanceof StockSplitEvent) {
      await service.doSecurityStocksplit({
        accountId : account.id,
        securityId: action.securityId,
        quantity : action.quantity
      });  
    }
    

    dispatch(action);
   }

  if (!account) {
    return(<></>);
  }

  return (
    <>       
         
        <div className="grid grid-cols-15 gap-1">
          <div className="col-span-4 rounded-md bg-amber-400 p-2">{account.id} ({account.owner})</div>          
          <div className="rounded-md bg-amber-400 p-2 text-right">
            <input name="allocation" min="0" step="1" type="number" onChange={(event) => handleAccountEvent(event.nativeEvent, new ModifyAccountAllocationAmountEvent({allocationAmount : Number(event.target.value)}))} defaultValue={account.allocationAmount} className="border-black w-20 text-right"></input>
          </div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.balanceAmount.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netCost.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.marketValue.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.saleFee.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netProceeds.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gains.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gainsPerncetage.toFixed(2)}</div>
          <div className="col-span-3 rounded-md bg-amber-400 p-2">
            
          </div>

          {account.sectors.map((sector,index) => (
            <>
              <SectorSnapshotComponent 
              key = { sector.name }
              sector = { sector } 
              accountEventHandler = { handleAccountEvent }
              />
              {
                sector.securities.map((security,i) => (
                  <>
                    <SecuritySnapshotComponent 
                    key={security.id}
                    accountEventHandler = { handleAccountEvent }
                    security = {security}/>
                  </>
                ))
              }             
            </> 
          ))}
        </div>      
    </>  
  );
}