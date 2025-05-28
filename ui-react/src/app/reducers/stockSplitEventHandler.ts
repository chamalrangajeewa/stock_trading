import { produce } from "immer";
import { AccountSnapshot } from "../accountSnapshot";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

export class StockSplitEventHandler {

  handle(currentState: AccountSnapshotViewModel, event: any): AccountSnapshotViewModel {

    const nextState = produce(currentState, draft => {      
      let security = draft.sectors.map(o => o.securities.filter(i => i.id == event.id)).flat()[0];

      if (security) {
        let currentNetCost = security.quantity * security.averagePerUnitCost;
        security.quantity = event.quantity;
        let newAverageUnitPrice = currentNetCost/event.quantity;
        security.averagePerUnitCost = newAverageUnitPrice;
      }         
    });

    return nextState;
  }
}
