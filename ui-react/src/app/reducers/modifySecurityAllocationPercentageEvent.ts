export class ModifySecurityAllocationPercentageEvent {

  static readonly type: string = 'ModifySecurityAllocationPercentageEvent';
  readonly type : string = ModifySecurityAllocationPercentageEvent.type;
  
  allocationPercentage: number = 0;
  securityId: string = '';
 
  constructor(values:{securityId : string, allocationPercentage:number}){
    Object.assign(this, values);
  }
}
