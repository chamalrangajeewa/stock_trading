import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class ModifySectorAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    console.log('hello from ModifySectorAllocationPercentageEventHandler',currentState);
    return currentState;
  }
}
