'use client';

import  React from "react";
import { useState, useEffect } from "react";
import { SecuritySnapshot } from "../accountSnapshot";
import { SecuritySnapshotViewModel } from "./securitySnapshotViewModel";
import { ModifySecurityAllocationPercentageEvent } from "../reducers/modifySecurityAllocationPercentageEvent";
import { StockSplitEvent } from "../reducers/stockSplitEvent";

export interface SecurityProps {
  security: SecuritySnapshotViewModel;
  accountEventHandler : (e:Event, payload:any) => void
}


export default function SecuritySnapshotComponent(props: SecurityProps) {

  let security = props.security;
  let handleAccountEvent = props.accountEventHandler;

  if (!props.security) {
    return(<></>);
  }

  return (
    <>
        <span className="col-span-3 rounded-md bg-blue-100">{security.name}({security.id})</span>
        <span className="rounded-md bg-blue-100 p-2 text-center">
          <input name="allocation" min="0" max="100" step="1" type="number" onChange={(event) => handleAccountEvent(event.nativeEvent, new ModifySecurityAllocationPercentageEvent({securityId:security.id, allocationPercentage: Number(event.target.value)}))} defaultValue={security.allocationPercentage} className="border-black w-11 text-right"></input>
        </span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.allocationAmount.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.balanceAmount.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.netCost.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.marketValue.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.saleFee.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.netProceeds.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.gains.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.gainsPerncetage.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">
          <input className="border-black w-17 text-right" name="allocation" min="0" step="1" type="number" onChange={(event) => handleAccountEvent(event.nativeEvent, new StockSplitEvent({securityId:security.id, quantity: Number(event.target.value)}))} defaultValue={security.quantity}></input>
        </span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.averagePerUnitCost.toFixed(2)}</span>
        <span className="rounded-md bg-blue-100 p-2 text-right">{security.livePerUnitCost.toFixed(2)}</span>
    </>  
  );
}
