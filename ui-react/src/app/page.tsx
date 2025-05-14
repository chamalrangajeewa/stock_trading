'use client';

import  React from "react";
import { useState, useEffect } from "react";
import { AccountSnapshot } from "./accountSnapshot";
import AccountSnapshotComponent from "./component/accountsnapshot";


export default function Home() {

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

  useEffect(() => {

    let ignore = false;
    setPortfolio(accountInitialState);

    async function fetchPortfolio() {
      const respose = await fetch("https://682383c365ba05803397073e.mockapi.io/api/cse/Account")
      if(!respose.ok)
        throw new Error("error loading");  

      const data = await respose.json();
      
      if(!ignore)
        setPortfolio(data);
    }

    fetchPortfolio();

    return () => {
      ignore = true;
    }
  }, []);


  return (
    <>
      <div className="p-4 overflow-auto">
      
      <AccountSnapshotComponent></AccountSnapshotComponent>

      {/* <div className="grid grid-cols-15 gap-1">
        <div className="col-span-15 rounded-md bg-amber-400 p-2">Header</div>

        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center">Sector</div>
        <div className="rounded-md bg-amber-100 p-2 text-left">30</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">25</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">20,000</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">12000</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">2300</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">22000</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">21000</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">21000</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">21000</div>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center"></div>

        <div className="col-span-3 rounded-md bg-red-200 p-2 text-center">Company (Security)</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Target</div>
        <div className="rounded-md bg-red-200 p-2 text-center">actual</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Amount</div>
        <div className="rounded-md bg-red-200 p-2 text-center">cost</div>
        <div className="rounded-md bg-red-200 p-2 text-center">sales fees</div>
        <div className="rounded-md bg-red-200 p-2 text-center">market value</div>
        <div className="rounded-md bg-red-200 p-2 text-center">proceeds</div>
        <div className="rounded-md bg-red-200 p-2 text-center">gains</div>
        <div className="rounded-md bg-red-200 p-2 text-center">gains %</div>
        <div className="rounded-md bg-red-200 p-2 text-center">qty</div>
        <div className="rounded-md bg-red-200 p-2 text-center">average price</div>
        <div className="rounded-md bg-red-200 p-2 text-center">live price</div>

        <span className="col-span-3 rounded-md bg-blue-100">SAMPATH BANK PLC</span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>

        <span className="col-span-3 rounded-md bg-blue-100">SAMPATH BANK PLC</span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
        <span className="rounded-md bg-blue-100"></span>
      </div> */}

      </div>   

    </>  
  );
}
