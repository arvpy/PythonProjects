posX=190 //setting the centre positions
posY=190 //setting the centre positions
var xSpeed = 4;
var ySpeed = 3;
score=0

function setup() {

  createCanvas(400, 400);

}

function draw() {

  background("red")
  rect(375, mouseY, 15, 90);
  rect(posX,posY,20,20);
  rect(0, posY, 15, 90)
  text("Score: " + score, 80, 25);
  text("Score:0 ", 280, 25);
  line(200,0,200,400)

  posX += xSpeed
  posY += ySpeed

  if (posX <= 10) {
    xSpeed *= -1;
  }

  if (posY <= 10 || posY >=390 ) {
    ySpeed *= -1;
  }
  if((posX >=365) && (posY>=mouseY && posY<=mouseY+90)){
   xSpeed *= -1;
   ySpeed *=-1;

  if(posX>390){
    score++
    posX=190
    posY=190


}
}

}
