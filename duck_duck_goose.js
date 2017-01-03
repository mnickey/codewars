/**
 * Created by MNickey on 1/2/17.
 * Duck Duck Goose
 * JavaScript
 */


function duckDuckGoose(players, goose) {

    while (players.length < goose) {
        goose -= players.length
    }
    return players[goose - 1].name
}