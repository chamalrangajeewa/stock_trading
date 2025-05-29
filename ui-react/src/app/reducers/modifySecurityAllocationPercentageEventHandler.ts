import { produce } from "immer";
import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class ModifySecurityAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    const nextState = produce(currentState, draft => {      
      let security = draft.sectors.map(o => o.securities.filter(i => i.id == event.securityId)).flat()[0];

      if (security) {
        security.allocationPercentage = event.allocationPercentage;
      }
      draft.reevaluateCalculatedFeilds();    
    });
    
    return nextState;
  }
}
