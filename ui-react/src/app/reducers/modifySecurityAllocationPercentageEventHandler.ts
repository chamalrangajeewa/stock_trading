import { AccountSnapshot } from "../accountSnapshot";

export class ModifySecurityAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshot, event: any): AccountSnapshot {

    console.log('hello from ModifySecurityAllocationPercentageEventHandler',currentState);
    return currentState;
  }
}
