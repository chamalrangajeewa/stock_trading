// import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshot } from "./accountSnapshot";
import { ModifyInvestmentAllocationAmountRequest } from "./ModifyInvestmentAllocationAmountRequest";
import { ModifySectorAllocationPercentageRequest } from "./ModifySectorAllocationPercentageRequest";
import { ModifySecurityAllocationPercentageRequest } from "./ModifySecurityAllocationPercentageRequest";

export class AccountService {
    constructor(private baseUrl:string = "http://127.0.0.1:8000") {
        
    }

    async get(accountId:string) {
        const url = `${this.baseUrl}/account/dashboard`;
        const respose = await fetch(url);
        
        if(!respose.ok)
            throw new Error("error loading");  

        const data : AccountSnapshot  = await respose.json();
        return data;
    }

    async modifyAccountInvestmentAllocationAmount( payload : ModifyInvestmentAllocationAmountRequest): Promise<void> {
        const url = `${this.baseUrl}/account/modify-allocation-amount`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async modifySectorAllocationPercentage( payload : ModifySectorAllocationPercentageRequest): Promise<void> {
        const url = `${this.baseUrl}/sector/modify-allocation-percentage`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async modifySecurityAllocationPercentage( payload : ModifySecurityAllocationPercentageRequest): Promise<void> {
        const url = `${this.baseUrl}/security/modify-allocation-percentage`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

    async doSecurityStocksplit( payload : ModifySecurityAllocationPercentageRequest): Promise<void> {
        const url = `${this.baseUrl}/security/do-stock-split`;
        const respose = await fetch(url, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        
        if(!respose.ok)
            throw new Error("error loading");  
    }

}