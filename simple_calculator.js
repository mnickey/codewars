/**
 * Created by MNickey on 1/2/17.
simple calculator
JavaScript
 */

function calculator(a,b,sign){
    if (parseInt(a) && parseInt(b)) {
        if (sign == "+") {
            return a+b;
        }
        else if (sign == "-") {
            return a - b;
            }
        else if (sign == "*") {
            return a * b;
        }
        else if (sign == "/") {
            return a / b;
        }
        else {
            return "unknown value";
            }
    }
    else return "unknown value";
}