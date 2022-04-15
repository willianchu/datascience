const e = 50
let north = 0;
let east = 500;
function setup() {
  createCanvas(500, 500);
  background(455);
  for (let i = 0; i < 501; i += 50) {
    line(i, 0, i, 500);
    line(0, i, 500, i);
  }
  const blocksAway = function (directions) {
    strokeWeight(4)
    let facingDirection = "";
    if (directions[0] === "right") {
      north = north + directions[1];
      facingDirection = "north";
      stroke("red"); // starter
      line(0, east, north, east); // go south ?
    } else if (directions[0] === "left") {
      east = east - directions[1];
      facingDirection = "east";
      stroke("pink");
      line(north, east, north, 500); // go north
    }
    console.log("starter"+facingDirection)

    for (let i = 2; i < directions.length; i += 2) {
      console.log("Loop"+i+facingDirection)
      if (facingDirection === "north") {
        if (directions[i] === "right") {
          east = east + directions[i + 1];
          facingDirection = "west";
          stroke("green"); // direction west >> east
          line(north, east - directions[i + 1], north, east); // go south
          continue;
        } else if (directions[i] === "left") {
          east = east - directions[i + 1];
          facingDirection = "east";
          stroke("lightgreen");
          line(north, east + directions[i + 1], north, east); // go north ?
          continue;
        }
      }
      if (facingDirection === "east") {
        if (directions[i] === "right") {
          north = north + directions[i + 1];
          facingDirection = "north";
          stroke("blue"); // from south >> north
          line(north - directions[i + 1], east, north, east); // go east
          continue;
        } else if (directions[i] === "left") {
          north = north - directions[i + 1];
          facingDirection = "south";
          stroke("lightblue");
          line(north + directions[i + 1], east, north, east); // go west?
          continue;
        }
      }
      if ((facingDirection === "south")) {
        if (directions[i] === "right") {
          east = east - directions[i + 1];
          facingDirection = "east";
          stroke("brown");
          line(north, east + directions[i + 1], north, east); // probl upp
          continue;
        } else if (directions[i] === "left") {
          east = east + directions[i + 1];
          facingDirection = "west";
          stroke("orange");
          line(north, east - directions[i + 1], north, east);
          continue;
        }
      }
      if (facingDirection === "west") {
        console.log("We're heading WEST !!!!");
        if (directions[i] === "right") {
          north = north - directions[i + 1];
          facingDirection = "south";
          stroke("red");
          line(north + directions[i + 1], east, north, east);
          continue;
        } else if (directions[i] === "left") {
          north = north + directions[i + 1];
          facingDirection = "north";
          stroke("grey");
          line(north - directions[i + 1], east, north, east);
          continue;
        }
      }
    }
    stroke(0);
    ellipse(north, east, 10, 10);
  };
  // change single digit values
  blocksAway(["right", 4 * e, "left", 4 * e, "right", 1 * e, "right", 3 * e, "right", 1 * e]);
}