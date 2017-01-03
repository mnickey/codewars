/**
 * Created by MNickey on 1/2/17.
 * What's up next?
 * JavaScript
 */

function nextItem(xs, item) {
    var found = false;
    for (var x of xs) {
        if (found) return x;
        if (x == item) found = true;
    }
    return undefined;
}