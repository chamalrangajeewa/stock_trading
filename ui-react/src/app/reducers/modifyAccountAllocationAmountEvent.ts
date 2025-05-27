
export class ModifyAccountAllocationAmountEvent {
  
  static readonly type: string = 'ModifyAccountAllocationAmountEvent';
  readonly type : string = ModifyAccountAllocationAmountEvent.type;
  id: string = '';
  allocationAmount: number = 0;

  constructor(values:{id:string , allocationAmount:number}){
    Object.assign(this, values);
  }
}
