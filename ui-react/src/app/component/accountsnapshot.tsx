'use client';

import { useReducer } from 'react';
import  React from "react";
import SectorSnapshotComponent from "./sectorsnapshot";
import SecuritySnapshotComponent from "./securitysnapshot";
import { AccountSnapshot } from "../accountSnapshot";
import { accountReducer } from '../reducers/accountReducer';
import { StockSplitEvent } from '../reducers/stockSplitEvent';
import { ModifyAccountAllocationAmountEvent } from '../reducers/modifyAccountAllocationAmountEvent';
import { ModifySectorAllocationPercentageEvent } from '../reducers/modifySectorAllocationPercentageEvent';
import { ModifySecurityAllocationPercentageEvent } from '../reducers/modifySecurityAllocationPercentageEvent';

export interface AccountProps {
  account?: AccountSnapshot;
}

export default function AccountSnapshotComponent(props: AccountProps) {
   
  const [account, dispatch] = useReducer(accountReducer, props.account);

  function handleAccountEvent(e:Event, payload:any) {
    debugger;
    e.stopPropagation();
    console.log("payload", payload);
    dispatch(payload);
   }

   function handleSyncUnitPriceClick(e:Event, payload:any) {
    e.stopPropagation();
    dispatch(payload);
   }

  if (!account) {
    return(<></>);
  }

  return (
    <>                
        <div className="grid grid-cols-15 gap-1">
          <div className="col-span-4 rounded-md bg-amber-400 p-2">{account.id} ({account.owner})</div>          
          <div className="rounded-md bg-amber-400 p-2 text-right">
            <input name="allocation" min="0" step="1" type="number" onChange={(event) => handleAccountEvent(event.nativeEvent, new ModifyAccountAllocationAmountEvent({id:account.id, allocationAmount: Number(event.target.value)}))} defaultValue={account.allocationAmount} className="border-black w-20 text-right"></input>
          </div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.balanceAmount.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netCost.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.marketValue.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.saleFee.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netProceeds.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gains.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gainsPerncetage.toFixed(2)}</div>
          <div className="col-span-3 rounded-md bg-amber-400 p-2">
            <button className="rounded-md bg-red-200" onClick= {(evt) => handleSyncUnitPriceClick(evt, new StockSplitEvent())}>stocksplit</button>
            <button className="rounded-md bg-red-200" onClick={(evt) => handleSyncUnitPriceClick(evt, new ModifyAccountAllocationAmountEvent({id:account.id, allocationAmount: 10}))}>account allocation</button>
            <button className="rounded-md bg-red-200" onClick={(evt) => handleSyncUnitPriceClick(evt, new ModifySectorAllocationPercentageEvent())}>sectors %</button>
            <button className="rounded-md bg-red-200" onClick={(evt) => handleSyncUnitPriceClick(evt, new ModifySecurityAllocationPercentageEvent())}>Security %</button>         
          </div>

          {account.sectors.map((sector,index) => (
            <>
              <SectorSnapshotComponent 
              key = {index}
              sector = { sector }  
              />
              {
                sector.securities.map((security,i) => (
                  <>
                    <SecuritySnapshotComponent 
                    key={security.id}
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