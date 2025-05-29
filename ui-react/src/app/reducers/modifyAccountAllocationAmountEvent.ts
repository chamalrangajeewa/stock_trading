export class ModifyAccountAllocationAmountEvent {
  
  static readonly type: string = 'ModifyAccountAllocationAmountEvent';
  readonly type : string = ModifyAccountAllocationAmountEvent.type;
  
  allocationAmount: number = 0;

  constructor(values:{allocationAmount : number}){
    Object.assign(this, values);
  }
}
