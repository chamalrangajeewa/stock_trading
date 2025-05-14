
export class SecuritySnapshot {

    name : string = '';
    id : string = '';    
    allocationPercentage: number = 0;
    allocationAmount : number = 0;
    balanceAmount : number = 0;
    netCost : number = 0;
    marketValue : number = 0;
    saleFee : number = 0;
    netProceeds : number = 0;
    gains: number = 0;
    gainsPerncetage:number = 0;
    quantity : number = 0;
    averagePerUnitCost : number = 0
    livePerUnitCost : number = 0;

}

export class SectorSnapshot {

    name : string = '';
    securities : SecuritySnapshot[] = [];
    allocationPercentage: number = 0;
    allocationAmount : number = 0;
    balanceAmount : number = 0;
    netCost : number = 0;
    marketValue : number = 0;
    saleFee : number = 0;
    netProceeds : number = 0;
    gains: number = 0;
    gainsPerncetage:number = 0;
}

export class AccountSnapshot {
    
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
    sectors : SectorSnapshot[] = [];
}