import { produce } from "immer";
import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class ModifySectorAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    const nextState = produce(currentState, draft => {      
      let sector = draft.sectors.find(o => o.name === event.id);

      if (sector) {
        sector.allocationPercentage = event.allocationPercentage;
      }
      draft.reevaluateCalculatedFeilds();    
    })
    
    return nextState;
  }
}
