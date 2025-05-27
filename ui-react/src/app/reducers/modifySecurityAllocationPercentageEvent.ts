
export class ModifySecurityAllocationPercentageEvent {

  static readonly type: string = 'ModifySecurityAllocationPercentageEvent';
  readonly type : string = ModifySecurityAllocationPercentageEvent.type;
  id: string = '';
  allocationPercentage: number = 0;

  constructor(values:{id:string , allocationPercentage:number}){
    Object.assign(this, values);
  }
}
