import { immerable } from "immer";
import { SecuritySnapshot } from "../service/accountSnapshot";

export class SecuritySnapshotViewModel {

    [immerable] = true;
    name: string = '';
    id: string = '';
    allocationPercentage: number = 0;
    allocationAmount: number = 0;
    balanceAmount: number = 0;
    netCost: number = 0;
    marketValue: number = 0;
    saleFee: number = 0;
    netProceeds: number = 0;
    gains: number = 0;
    gainsPerncetage: number = 0;
    quantity: number = 0;
    averagePerUnitCost: number = 0;
    livePerUnitCost: number = 0;

    constructor(o : SecuritySnapshot){

        this.name = o.name;
        this.id = o.id;
        this.allocationPercentage = o.allocationPercentage;
        this.allocationAmount = o.allocationAmount;
        this.balanceAmount = o.balanceAmount;
        this.netCost = o.netCost;
        this.marketValue =o.marketValue;
        this.saleFee =o.saleFee;
        this.netProceeds=o.netProceeds;
        this.gains=o.gains;
        this.gainsPerncetage=o.gainsPerncetage;
        this.quantity=o.quantity;
        this.averagePerUnitCost=o.averagePerUnitCost;
        this.livePerUnitCost=o.livePerUnitCost;
    }

    clone() : SecuritySnapshotViewModel{
                
        let o = new SecuritySnapshotViewModel(new SecuritySnapshot());
        
        o.name = this.name;
        o.id = this.id;
        o.allocationPercentage = this.allocationPercentage;
        o.allocationAmount = this.allocationAmount;
        o.balanceAmount = this.balanceAmount;
        o.netCost = this.netCost;
        o.marketValue =this.marketValue;
        o.saleFee =this.saleFee;
        o.netProceeds=this.netProceeds;
        o.gains=this.gains;
        o.gainsPerncetage=this.gainsPerncetage;
        o.quantity=this.quantity;
        o.averagePerUnitCost=this.averagePerUnitCost;
        o.livePerUnitCost=this.livePerUnitCost;
                
        return o;
    }

}
