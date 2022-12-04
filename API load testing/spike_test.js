import http from "k6/http";
import {sleep} from "k6";

export let options = {
    insecureSkipTLSVerify: true,
    noConnectionReuse: false,

    stages: [
        {duration: "10s" , target: 100 }, //below normal load
        {duration: "1m" , target: 100 },
        {duration: "10s" , target: 1400 }, //spike
        {duration: "3m" , target: 1400 },
        {duration: "10s" , target: 100 }, //recovery stage
        {duration: "3m" , target: 100 },
        {duration: "10s" , target: 0 },
        
    ]
};

export default() => {

    http.get("https://test.k6.io");
    sleep(1);
};