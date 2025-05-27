import {produce} from "immer"
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";
import { AccountSnapshot } from "../service/accountSnapshot";

export class ModifyAccountAllocationAmountEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    debugger;
    // const nextState = produce(currentState, draft => {      
    //   draft.allocationAmount = event.allocationAmount;      
    //   draft.reevaluateCalculatedFeilds();    
    // })
    
    const nextState1 = currentState.clone();
    nextState1.allocationAmount = event.allocationAmount;
    nextState1.reevaluateCalculatedFeilds();
    
    
    console.log('ModifyAccountAllocationAmountEventHandler currentState', currentState);
    console.log('ModifyAccountAllocationAmountEventHandler nextState', nextState1);
    return nextState1;
  }
}
