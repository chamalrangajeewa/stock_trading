'use client';

import  React from "react";
import { useState, useEffect } from "react";
import SectorSnapshotComponent from "./sectorsnapshot";
import SecuritySnapshotComponent from "./securitysnapshot";
import { AccountSnapshot } from "../accountSnapshot";

export default function AccountSnapshotComponent({ account1 }) {
  
  const account : AccountSnapshot = account1;      
  if (!account) {
    return(<></>);
  }

  return (
    <>                
        <div className="grid grid-cols-15 gap-1">
          <div className="col-span-4 rounded-md bg-amber-400 p-2">{account.id} ({account.owner})</div>          
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.allocationAmount.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.balanceAmount.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netCost.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.marketValue.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.saleFee.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.netProceeds.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gains.toFixed(2)}</div>
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gainsPerncetage.toFixed()}</div>
          <div className="col-span-3 rounded-md bg-amber-400 p-2"></div>

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
