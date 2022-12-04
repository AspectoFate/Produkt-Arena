import http from "k6/http";
import {sleep} from "k6";

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,

    stages: [
        {duration: "2m" , target: 400 }, //simulate ramp-up traffic
        {duration: "3h56m" , target: 400 }, // stay at 400 users for aprox 4 hours
        {duration: "5m" , target: 0 }, //recovery
        
    ],
    
};

export default() => {

    http.get("https://test.k6.io");
    sleep(1);
};