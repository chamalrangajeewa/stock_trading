'use client';

import  React from "react";
import { useState, useEffect } from "react";
import SectorSnapshotComponent from "./sectorsnapshot";
import SecuritySnapshotComponent from "./securitysnapshot";
import { AccountSnapshot } from "../accountSnapshot";

export default function AccountSnapshotComponent() {

  const accountInitialState : AccountSnapshot = 
      {
        "id": "CAS/104948-LI/0",
        "owner": "Chamal Janindra",
        "allocationAmount": 10000,
        "balanceAmount": 400,
        "netCost" : 0,
        "marketValue" : 0,
        "saleFee" : 0,
        "netProceeds" : 0,
        "gains": 0,
        "gainsPerncetage": 0,
        "sectors": [
          {
            "name": "Diversified Financials",
            "allocationPercentage" : 50,
            "allocationAmount": 5000,
            "balanceAmount": 400,
            "netCost" : 0,
            "marketValue" : 0,
            "saleFee" : 0,
            "netProceeds" : 0,
            "gains": 0,
            "gainsPerncetage": 0,
            "securities": [
              {
                "id": "AAF.N0000",
                "name": "ASIA ASSET FINANCE PLC",
                "allocationPercentage" : 50,
                "allocationAmount": 2500,
                "balanceAmount": 400,
                "netCost" : 0,
                "marketValue" : 0,
                "saleFee" : 0,
                "netProceeds" : 0,
                "gains": 0,
                "gainsPerncetage": 0,
                "quantity": 2,
                "averagePerUnitCost": 2.44,
                "livePerUnitCost": 20.44
              },
              {
                "id": "AAIC.N0000",
                "name": "SOFTLOGIC LIFE INSURANCE PLC",
                "allocationPercentage" : 50,
                "allocationAmount": 2500,
                "balanceAmount": 400,
                "netCost" : 0,
                "marketValue" : 0,
                "saleFee" : 0,
                "netProceeds" : 0,
                "gains": 0,
                "gainsPerncetage": 0,
                "quantity": 2,
                "averagePerUnitCost": 2.44,
                "livePerUnitCost": 20.44
              }
            ]
          },
          {
            "name": "Materials",
            "allocationPercentage" : 50,
            "allocationAmount": 5000,
            "balanceAmount": 400,
            "netCost" : 0,
            "marketValue" : 0,
            "saleFee" : 0,
            "netProceeds" : 0,
            "gains": 0,
            "gainsPerncetage": 0,
            "securities": [
              {
                "id": "ABAN.N0000",
                "name": "ABANS ELECTRICALS PLC",
                "allocationPercentage" : 50,
                "allocationAmount": 2500,
                "balanceAmount": 400,
                "netCost" : 0,
                "marketValue" : 0,
                "saleFee" : 0,
                "netProceeds" : 0,
                "gains": 0,
                "gainsPerncetage": 0,
                "quantity": 2,
                "averagePerUnitCost": 2.44,
                "livePerUnitCost": 20.44
              },
              {
                "id": "ABL.N0000",
                "name": "AMANA BANK PLC",
                "allocationPercentage" : 50,
                "allocationAmount": 2500,
                "balanceAmount": 400,
                "netCost" : 0,
                "marketValue" : 0,
                "saleFee" : 0,
                "netProceeds" : 0,
                "gains": 0,
                "gainsPerncetage": 0,
                "quantity": 2,
                "averagePerUnitCost": 2.44,
                "livePerUnitCost": 20.44
              }
            ]
          }
        ]
      }
  
      
  const [portfolio, setPortfolio] = useState(accountInitialState);

  return (
    <>
        <div className="grid grid-cols-15 gap-1">
          <div className="col-span-4 rounded-md bg-amber-400 p-2">{portfolio.id} ({portfolio.owner})</div>          
          <div className="rounded-md bg-amber-400 p-2">{portfolio.allocationAmount}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.balanceAmount}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.netCost}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.marketValue}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.saleFee}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.netProceeds}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.gains}</div>
          <div className="rounded-md bg-amber-400 p-2">{portfolio.gainsPerncetage}</div>
          <div className="col-span-3 rounded-md bg-amber-400 p-2"></div>
          

          {accountInitialState.sectors.map((sector,index) => (
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
