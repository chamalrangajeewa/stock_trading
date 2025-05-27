import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class ModifySecurityAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    console.log('hello from ModifySecurityAllocationPercentageEventHandler',currentState);
    return currentState;
  }
}
