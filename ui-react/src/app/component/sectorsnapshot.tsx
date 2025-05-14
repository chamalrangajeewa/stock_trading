'use client';

import  React from "react";
import { useState, useEffect } from "react";
import HeaderComponent from "./header";
import { SectorSnapshot } from "../accountSnapshot";
export default function SectorSnapshotComponent({ sector }) {

  const initialState : SectorSnapshot = sector;
  const [portfolio, setPortfolio] = useState(initialState);
  // debugger;

  return (
    <>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center">{portfolio.name}</div>
        <div className="rounded-md bg-amber-100 p-2 text-left">{portfolio.allocationPercentage}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.allocationAmount}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.balanceAmount}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.netCost}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.marketValue}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.saleFee}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.netProceeds}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.gains}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">{portfolio.gainsPerncetage}</div>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center"></div>
        <HeaderComponent/>
    </>  
  );
}
