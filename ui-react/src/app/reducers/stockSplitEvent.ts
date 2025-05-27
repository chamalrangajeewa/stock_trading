
export class StockSplitEvent {

  static readonly type: string = 'StockSplitEvent';
  readonly type : string = StockSplitEvent.type;
  id: string = '';
  quantity: number = 0;

  constructor(values:{id:string , quantity:number}){
    Object.assign(this, values);
  }
}