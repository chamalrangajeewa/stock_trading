// import { AccountSnapshot } from "../accountSnapshot";
// import { StockSplitEvent } from "../reducers/stockSplitEvent";
import { AccountSnapshot } from "./accountSnapshot";
import { ModifyInvestmentAllocationAmountRequest } from "./modifyInvestmentAllocationAmountRequest";
import { ModifySectorAllocationPercentageRequest } from "./modifySectorAllocationPercentageRequest";
import { ModifySecurityAllocationPercentageRequest } from "./modifySecurityAllocationPercentageRequest";
import { StocksplitRequest } from "./stocksplitRequest";

export class AccountService {
    constructor(private baseUrl:string = "http://127.0.0.1:8000") {
        
    }

    async get(accountId:string) {
        const url = `${this.baseUrl}/portfolio/view?accountId=${accountId}`;
        const respose = await fetch(url);
        
        if(!respose.ok)
            throw new Error("error loading");  

        const data : AccountSnapshot  = await respose.json();
        return data;
    }

    async modifyAccountInvestmentAllocationAmount( payload : ModifyInvestmentAllocationAmountRequest): Promise<void> {
        const url = `${this.baseUrl}/portfolio/adjust-allocation-amount`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async modifySectorAllocationPercentage( payload : ModifySectorAllocationPercentageRequest): Promise<void> {
        const url = `${this.baseUrl}/portfolio/sector/adjust-allocation-percentage`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async modifySecurityAllocationPercentage( payload : ModifySecurityAllocationPercentageRequest): Promise<void> {
        const url = `${this.baseUrl}/portfolio/security/adjust-allocation-percentage`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async doSecurityStocksplit( payload : StocksplitRequest): Promise<void> {
        const url = `${this.baseUrl}/portfolio/security/stocksplit`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }
}