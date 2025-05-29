'use client';

import  React from "react";
import { useState, useEffect } from "react";
import HeaderComponent from "./header";
import { SectorSnapshot } from "../accountSnapshot";
import { SectorSnapshotViewModel } from "./sectorSnapshotViewModel";
import { ModifySectorAllocationPercentageEvent } from "../reducers/modifySectorAllocationPercentageEvent";

export interface SectorProps {
  sector: SectorSnapshotViewModel;
  accountEventHandler : (e:Event, payload:any) => void
}

export default function SectorSnapshotComponent(props: SectorProps) {

  let sector = props.sector;
  let handleAccountEvent = props.accountEventHandler;

  if (!props.sector) {
    return(<></>);
  }

  return (
    <>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center">{sector.name}</div>
        <div className="rounded-md bg-amber-100 p-2 text-center">
          <input name="allocation" min="0" max="100" step="1" type="number" onChange={(event) => handleAccountEvent(event.nativeEvent, new ModifySectorAllocationPercentageEvent({name:sector.name, allocationPercentage: Number(event.target.value)}))} defaultValue={sector.allocationPercentage} className="border-black w-11 text-right"></input>         
        </div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.allocationAmount.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.balanceAmount.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.netCost.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.marketValue.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.saleFee.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.netProceeds.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.gains.toFixed(2)}</div>
        <div className="rounded-md bg-amber-100 p-2 text-right">{sector.gainsPerncetage.toFixed(2)}</div>
        <div className="col-span-3 rounded-md bg-amber-100 p-2 text-center"></div>
        <HeaderComponent/>
    </>  
  );
}
