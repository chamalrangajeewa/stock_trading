
export class ModifySectorAllocationPercentageEvent {

  static readonly type: string = 'ModifySectorAllocationPercentageEvent';
  readonly type : string = ModifySectorAllocationPercentageEvent.type;
  id: string = '';
  allocationPercentage: number = 0;

  constructor(values:{id:string , allocationPercentage:number}){
    Object.assign(this, values);
  }
}
