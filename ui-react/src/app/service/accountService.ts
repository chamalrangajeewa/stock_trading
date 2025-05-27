import { AccountSnapshot } from "../accountSnapshot";

// export const getTodos = async () => {
//   const response = await axios.get("http://localhost:3004/todos");
//   return response.data;
// };

export class AccountService {
    constructor(private baseUrl:string = "http://127.0.0.1:8000") {
        
    }

    async get(accountId:string) {
        const url = `${this.baseUrl}/account/dashboard`;
        const respose = await fetch(url);
        
        if(!respose.ok)
            throw new Error("error loading");  

        const data : AccountSnapshot  = await respose.json();
        return data;
    }

}