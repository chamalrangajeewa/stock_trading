import { AccountSnapshot } from "../accountSnapshot";

export class ModifyAccountAllocationAmountEventHandler {

  handle(currentState: AccountSnapshot  | undefined | null, event: any): AccountSnapshot  | undefined | null {

    console.log('hello from ModifyAccountAllocationAmountEventHandler', currentState);
    
    let result = new AccountSnapshot();
    result.allocationAmount = event.allocationAmount;
    return result;
  }
}
