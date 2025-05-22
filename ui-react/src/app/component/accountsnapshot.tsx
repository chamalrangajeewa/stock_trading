'use client';

import  React from "react";
import SectorSnapshotComponent from "./sectorsnapshot";
import SecuritySnapshotComponent from "./securitysnapshot";
import { AccountSnapshot } from "../accountSnapshot";

export default function AccountSnapshotComponent({ account1 }) {
   
  function handleSyncUnitPriceClick(e:Event) {
    e.stopPropagation();

    alert('You clicked me!');

    const init = { 
      headers: new Headers({
      "content-type": "application/json",
      "referer" :"https://www.cse.lk/",
      "origin" : "https://www.cse.lk"
      }),
      method : "POST",
      body: JSON.stringify({
        "headerse": {
          "normalizedNames":{},
          "lazyUpdate":null
        }
      })
    };

    const request = new Request("https://www.cse.lk/api/tradeSummary", init);
    fetch(request)
    .then((response: Response) => {
      if(!response.ok){
        throw new Error(`HTTP error, status = ${response.status}`);
      }
      return response.json();
    })
    .catch((error) => console.error(error))
    // const respose = fetch(request)
    // .then((resp) => {
    //       if (!resp.ok) {
    //         throw new Error(`HTTP error, status = ${resp.status}`);
    //       }

    //       return resp.json();
    //     })
    //     .then((data) => console.error(data))
    //     .catch((error) => console.error(error))
  }

  // function save(data: any){

  //   const init = { 
  //     headers: new Headers({
  //     "content-type": "application/json",
  //     }),
  //     method : "POST",
  //     body: JSON.stringify(data)
  //   };

  //   const request = new Request("http://127.0.0.1:8000/account/syncprice", init);
  //   const respose = fetch(request)
  //   .then((resp) => {
  //         if (!resp.ok) {
  //           throw new Error(`HTTP error, status = ${resp.status}`);
  //         }
  //       })
  // }
  
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
          <div className="rounded-md bg-amber-400 p-2 text-right">{account.gainsPerncetage.toFixed(2)}</div>
          <div className="col-span-3 rounded-md bg-amber-400 p-2"><button className="rounded-md bg-red-200" onClick={handleSyncUnitPriceClick}>Sync Unit Price</button></div>

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