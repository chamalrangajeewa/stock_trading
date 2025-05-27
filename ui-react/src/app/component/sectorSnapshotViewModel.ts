import { immerable } from "immer";
import { SectorSnapshot } from "../service/accountSnapshot";
import { SecuritySnapshotViewModel } from "./securitySnapshotViewModel";

export class SectorSnapshotViewModel {

    [immerable] = true;
    name: string = '';
    securities: SecuritySnapshotViewModel[] = [];
    allocationPercentage: number = 0;
    allocationAmount: number = 0;
    balanceAmount: number = 0;
    netCost: number = 0;
    marketValue: number = 0;
    saleFee: number = 0;
    netProceeds: number = 0;
    gains: number = 0;
    gainsPerncetage: number = 0;

    constructor(o : SectorSnapshot){
        this.securities = o.securities.map(i => new SecuritySnapshotViewModel(i));
        this.name = o.name;
        this.allocationPercentage = o.allocationPercentage;
        this.allocationAmount = o.allocationAmount;
        this.balanceAmount = o.balanceAmount;
        this.netCost = o.netCost;
        this.marketValue =o.marketValue;
        this.saleFee =o.saleFee;
        this.netProceeds=o.netProceeds;
        this.gains=o.gains;
        this.gainsPerncetage=o.gainsPerncetage;
    }

    clone() : SectorSnapshotViewModel{
            
            let o = new SectorSnapshotViewModel(new SectorSnapshot());
            
            o.name = this.name;
            o.allocationPercentage = this.allocationPercentage;
            o.allocationAmount = this.allocationAmount;
            o.balanceAmount = this.balanceAmount;
            o.netCost = this.netCost;
            o.marketValue =this.marketValue;
            o.saleFee =this.saleFee;
            o.netProceeds=this.netProceeds;
            o.gains=this.gains;
            o.gainsPerncetage=this.gainsPerncetage;
            o.securities = this.securities.map(i => i.clone());
            return o;
    }
}
