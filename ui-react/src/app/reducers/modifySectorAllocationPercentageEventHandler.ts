import { AccountSnapshot } from "../accountSnapshot";

export class ModifySectorAllocationPercentageEventHandler {

  handle(currentState: AccountSnapshot, event: any): AccountSnapshot {

    console.log('hello from ModifySectorAllocationPercentageEventHandler',currentState);
    return currentState;
  }
}
