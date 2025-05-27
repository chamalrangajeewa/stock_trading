import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class StockSplitEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    console.log('hello from stocksplit',currentState);
    return currentState;
  }
}
