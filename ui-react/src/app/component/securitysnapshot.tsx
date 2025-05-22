'use client';

import  React from "react";
import { useState, useEffect } from "react";
import { SecuritySnapshot } from "../accountSnapshot";
export default function SecuritySnapshotComponent({ security }) {

  const initialState : SecuritySnapshot = security;
  const [o, setSecurity] = useState(initialState);

  if (!security) {
    return(<></>);
  }

  return (
    <>
        <span className="col-span-3 rounded-md bg-blue-100">{o.name}({o.id})</span>
        <span className="rounded-md bg-blue-100 p-2 text-center">
          <input name="allocation" min="0" max="100" step="1" type="number" defaultValue={o.allocationPercentage} className="border-black w-11 text-right"></input>
        </span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.allocationAmount.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.balanceAmount.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.netCost.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.marketValue.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.saleFee.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.netProceeds.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.gains.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.gainsPerncetage.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.quantity}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.averagePerUnitCost.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{o.livePerUnitCost.toFixed(2)}</span>
    </>  
  );
}
