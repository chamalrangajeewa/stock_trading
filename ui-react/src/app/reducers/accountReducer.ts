import { AccountSnapshot } from "../accountSnapshot"
import { ModifySecurityAllocationPercentageEventHandler } from "./modifySecurityAllocationPercentageEventHandler";
import { StockSplitEventHandler } from "./stockSplitEventHandler";
import { ModifyAccountAllocationAmountEventHandler } from "./modifyAccountAllocationAmountEventHandler";
import { ModifySectorAllocationPercentageEventHandler } from "./modifySectorAllocationPercentageEventHandler";
import { ModifyAccountAllocationAmountEvent } from "./modifyAccountAllocationAmountEvent";
import { ModifySectorAllocationPercentageEvent } from "./modifySectorAllocationPercentageEvent";
import { ModifySecurityAllocationPercentageEvent } from "./modifySecurityAllocationPercentageEvent";
import { StockSplitEvent } from "./stockSplitEvent";

type eventType = ModifyAccountAllocationAmountEvent | 
                 ModifySectorAllocationPercentageEvent |
                 ModifySecurityAllocationPercentageEvent | 
                 StockSplitEvent               

const accountEventHandlers = new Map([
  [StockSplitEvent.type, new StockSplitEventHandler()],
  [ModifyAccountAllocationAmountEvent.type, new ModifyAccountAllocationAmountEventHandler()],
  [ModifySectorAllocationPercentageEvent.type, new ModifySectorAllocationPercentageEventHandler()],
  [ModifySecurityAllocationPercentageEvent.type, new ModifySecurityAllocationPercentageEventHandler()]
]);

export function accountReducer(account: AccountSnapshot | undefined | null , event: eventType ) {
  
  return accountEventHandlers.get(event.type)?.handle(account, event);
}