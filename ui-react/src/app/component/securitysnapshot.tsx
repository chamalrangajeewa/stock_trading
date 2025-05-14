'use client';

import  React from "react";
import { useState, useEffect } from "react";
import { SecuritySnapshot } from "../accountSnapshot";
export default function SecuritySnapshotComponent({ security }) {

  const initialState : SecuritySnapshot = security;
  const [o, setSecurity] = useState(initialState);

  return (
    <>
        <span className="col-span-3 rounded-md bg-blue-100">{o.name}({o.id})</span>
        <span className="rounded-md bg-blue-100">{o.allocationPercentage}</span>
        <span className="rounded-md bg-blue-100">{o.allocationAmount}</span>
        <span className="rounded-md bg-blue-100">{o.balanceAmount}</span>
        <span className="rounded-md bg-blue-100">{o.netCost}</span>
        <span className="rounded-md bg-blue-100">{o.marketValue}</span>
        <span className="rounded-md bg-blue-100">{o.saleFee}</span>
        <span className="rounded-md bg-blue-100">{o.netProceeds}</span>
        <span className="rounded-md bg-blue-100">{o.gains}</span>
        <span className="rounded-md bg-blue-100">{o.allocationPercentage}</span>
        <span className="rounded-md bg-blue-100">{o.quantity}</span>
        <span className="rounded-md bg-blue-100">{o.averagePerUnitCost}</span>
        <span className="rounded-md bg-blue-100">{o.livePerUnitCost}</span>
    </>  
  );
}
