export class StockSplitEvent {

  static readonly type: string = 'StockSplitEvent';
  readonly type : string = StockSplitEvent.type;

  securityId: string = '';
  quantity: number = 0;

  constructor(values:{securityId : string, quantity : number}){
    Object.assign(this, values);
  }
}