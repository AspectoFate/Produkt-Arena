import http from "k6/http";
import {sleep} from "k6";

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,

    stages: [
        {duration: "5m" , target: 100 }, //simulate ramp-up traffic
        {duration: "10m" , target: 100 }, // stay at 100 users for 10 min
        {duration: "5m" , target: 0 }, //recovery
        
    ],
    thresholds: {
        http_req_duration: ["p(99)<150"], //99% of req must be under 150 ms
    },
};

export default() => {

    http.get("https://test.k6.io");
    sleep(1);
};