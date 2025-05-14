'use client';

import  React from "react";
import { useState, useEffect } from "react";
export default function HeaderComponent() {

  const [portfolio, setPortfolio] = useState(null);

  return (
    <>
        <div className="col-span-3 rounded-md bg-red-200 p-2 text-center">Company (Security)</div>
        <div className="rounded-md bg-red-200 p-2 text-center">%</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Allocation</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Balance</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Net Cost</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Market Value</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Sale Fee</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Net Proceeds</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Gains</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Gains %</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Qty</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Average Price</div>
        <div className="rounded-md bg-red-200 p-2 text-center">Live Price</div>
    </>  
  );
}
