
export class StockSplitEvent {

  static readonly type: string = 'StockSplitEvent';
  readonly type : string = StockSplitEvent.type;
  id: string = '';
  quantity: number = 0;
}