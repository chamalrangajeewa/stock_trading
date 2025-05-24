import { AccountSnapshot } from "../accountSnapshot"

type eventType = ModifyAccountAllocationAmountEvent | 
                 ModifySectorAllocationPercentageEvent |
                 ModifySecurityAllocationPercentageEvent                

export class ModifyAccountAllocationAmountEvent {
    
    id : string = '';
    allocationAmount : number = 0;
}

export class ModifySectorAllocationPercentageEvent {
    
    id : string = '';
    allocationPercentage : number = 0;
}

export class ModifySecurityAllocationPercentageEvent {
    
    id : string = '';
    allocationPercentage : number = 0;
}

export class StockSplitEvent {
    
    id : string = '';
    quantity : number = 0 ;
}


class StockSplitEventHandler{

  handle(currentState: AccountSnapshot,  event:any): AccountSnapshot {
    
    return currentState;
  }
}

const accountEventHandlers = new Map([
  [typeof StockSplitEvent, new StockSplitEventHandler()]
]);

function accountReducer(account: AccountSnapshot, event : eventType ) {

  return accountEventHandlers.get(typeof event)?.handle(account, event);
}
