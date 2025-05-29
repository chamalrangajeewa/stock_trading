import {produce} from "immer"
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";
import { AccountSnapshot } from "../service/accountSnapshot";

export class ModifyAccountAllocationAmountEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {
      
    const nextState = produce(currentState, draft => {      
      draft.allocationAmount = event.allocationAmount;
      draft.reevaluateCalculatedFeilds();    
    })

    return nextState;
  }
}
