'use client';

import  React from "react";
import { useState, useEffect } from "react";
import HeaderComponent from "./header";
import { SectorSnapshot } from "../accountSnapshot";
export default function SectorSnapshotComponent({ sector }) {

  const initialState : SectorSnapshot = sector;
  const [portfolio, setPortfolio] = useState(initialState);

  if (!sector) {
    return(<></>);
  }

  return (
    <>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center">{portfolio.name}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">
          <input name="allocation" min="0" max="100" step="1" type="number" defaultValue={portfolio.allocationPercentage} className="border-black w-11 text-right"></input>         
        </div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.allocationAmount.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.balanceAmount.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.netCost.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.marketValue.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.saleFee.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.netProceeds.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.gains.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{portfolio.gainsPerncetage.toFixed(2)}</div>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center"></div>
        <HeaderComponent/>
    </>  
  );
}
