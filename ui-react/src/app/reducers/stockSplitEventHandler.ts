import { AccountSnapshot } from "../accountSnapshot";

export class StockSplitEventHandler {

  handle(currentState: AccountSnapshot, event: any): AccountSnapshot {

    console.log('hello from stocksplit',currentState);
    return currentState;
  }
}
