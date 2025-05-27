import { AccountSnapshot } from "../accountSnapshot"
import { ModifySecurityAllocationPercentageEventHandler } from "./modifySecurityAllocationPercentageEventHandler";
import { StockSplitEventHandler } from "./stockSplitEventHandler";
import { ModifyAccountAllocationAmountEventHandler } from "./modifyAccountAllocationAmountEventHandler";
import { ModifySectorAllocationPercentageEventHandler } from "./modifySectorAllocationPercentageEventHandler";
import { ModifyAccountAllocationAmountEvent } from "./modifyAccountAllocationAmountEvent";
import { ModifySectorAllocationPercentageEvent } from "./modifySectorAllocationPercentageEvent";
import { ModifySecurityAllocationPercentageEvent } from "./modifySecurityAllocationPercentageEvent";
import { StockSplitEvent } from "./stockSplitEvent";
import { AccountSnapshotViewModel } from "../component/accountSnapshotViewModel";

type eventType = ModifyAccountAllocationAmountEvent | 
                 ModifySectorAllocationPercentageEvent |
                 ModifySecurityAllocationPercentageEvent | 
                 StockSplitEvent               

const accountEventHandlers = new Map([
  [StockSplitEvent.type, new StockSplitEventHandler()]
  ,[ModifyAccountAllocationAmountEvent.type, new ModifyAccountAllocationAmountEventHandler()]
  ,[ModifySectorAllocationPercentageEvent.type, new ModifySectorAllocationPercentageEventHandler()]
  ,[ModifySecurityAllocationPercentageEvent.type, new ModifySecurityAllocationPercentageEventHandler()]
]);

export function accountReducer(account: AccountSnapshotViewModel, event: eventType ) {
  
  let hanldler = accountEventHandlers.get(event.type);
  
  if(hanldler)
    return hanldler.handle(account, event); 

  return account;
}