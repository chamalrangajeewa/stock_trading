export class ModifySectorAllocationPercentageEvent {

  static readonly type: string = 'ModifySectorAllocationPercentageEvent';
  readonly type : string = ModifySectorAllocationPercentageEvent.type;
  
  name: string = '';
  allocationPercentage: number = 0;

  constructor(values:{name : string, allocationPercentage : number}){
    Object.assign(this, values);
  }
}
