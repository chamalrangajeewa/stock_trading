import { immerable } from "immer";
import { AccountSnapshot } from "../service/accountSnapshot";
import { SectorSnapshotViewModel } from "./sectorSnapshotViewModel";

export class AccountSnapshotViewModel {
    
    [immerable] = true;
    id : string = '';
    owner : string = '';
    allocationAmount : number = 0;
    balanceAmount : number = 0;
    netCost : number = 0;
    marketValue : number = 0;
    saleFee : number = 0;
    netProceeds : number = 0;
    gains: number = 0;
    gainsPerncetage:number = 0;
    sectors : SectorSnapshotViewModel[] = [];

    constructor(o : AccountSnapshot){
        
        if(!o)
            return;

        this.sectors = o.sectors.map(i => new SectorSnapshotViewModel(i));
        this.id = o.id;
        this.owner = o.owner;
        this.allocationAmount = o.allocationAmount;
        this.balanceAmount = o.balanceAmount;
        this.netCost = o.netCost;
        this.marketValue =o.marketValue;
        this.saleFee =o.saleFee;
        this.netProceeds=o.netProceeds;
        this.gains=o.gains;
        this.gainsPerncetage=o.gainsPerncetage;
    }

    reevaluateCalculatedFeilds(){             

        for (let index = 0; index < this.sectors.length; index++) {
            const sector = this.sectors[index];
            sector.allocationAmount = this.allocationAmount * sector.allocationPercentage * 0.01;
        
            for (let i = 0; i < sector.securities.length; i++) {
                const security = sector.securities[i];

                security.allocationAmount = sector.allocationAmount * security.allocationPercentage * 0.01;
                security.netCost = security.averagePerUnitCost * security.quantity;
                security.marketValue = security.livePerUnitCost * security.quantity;
                security.balanceAmount = security.allocationAmount - security.netCost;
                security.saleFee = security.marketValue * 0.0112;
                security.netProceeds = security.marketValue - security.saleFee;
                security.gains = security.marketValue - security.saleFee - security.netCost;
                security.gainsPerncetage = (security.gains / security.netCost) * 100;        
            }

            sector.marketValue = sector.securities.map(o => o.marketValue).reduce((a,b) => a + b, 0);
            sector.saleFee = sector.securities.map(o => o.saleFee).reduce((a,b) => a + b, 0);
            sector.netCost = sector.securities.map(o => o.netCost).reduce((a,b) => a + b, 0);
            sector.netProceeds = sector.securities.map(o => o.netProceeds).reduce((a,b) => a + b, 0);
            sector.gains = sector.securities.map(o => o.gains).reduce((a,b) => a + b, 0);
            sector.gainsPerncetage = (sector.gains / sector.netCost) * 100; 
            sector.balanceAmount = sector.allocationAmount - sector.netCost;
            }

        this.marketValue = this.sectors.map(o => o.marketValue).reduce((a,b) => a + b, 0);
        this.saleFee = this.sectors.map(o => o.saleFee).reduce((a,b) => a + b, 0);
        this.netCost = this.sectors.map(o => o.netCost).reduce((a,b) => a + b, 0);
        this.netProceeds = this.sectors.map(o => o.netProceeds).reduce((a,b) => a + b, 0);
        this.gains = this.sectors.map(o => o.gains).reduce((a,b) => a + b, 0);
        this.gainsPerncetage = (this.gains / this.netCost) * 100; 
        this.balanceAmount = this.balanceAmount;
    }

    clone() : AccountSnapshotViewModel{
        let o = new AccountSnapshotViewModel(new AccountSnapshot());
        
        o.id = this.id;
        o.owner = this.owner;
        o.allocationAmount = this.allocationAmount;
        o.balanceAmount = this.balanceAmount;
        o.netCost = this.netCost;
        o.marketValue =this.marketValue;
        o.saleFee =this.saleFee;
        o.netProceeds=this.netProceeds;
        o.gains=this.gains;
        o.gainsPerncetage=this.gainsPerncetage;
        o.sectors = this.sectors.map(i => i.clone());

        return o;
    }
}