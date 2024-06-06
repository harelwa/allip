import processing.video.*;
Movie myMovie;
String videoFile;

void setup() {
    size(800, 600, P2D);
    // videoFile = "/home/altar/data/samples/short.mov";
    //videoFile = "/home/altar/pawns.court/altar.aleph/exports/D01.HAND.w.LAMP_1.mp4";
    videoFile = "/home/altar/pawns.court/altar.aleph/exports/D01.HAND.w.LAMP_1.mov";
    videoFile = "/home/altar/repos/allip/sandbox/loop/shorti.mov";
    videoFile = "/home/altar/repos/allip/sandbox/loop/D01.HAND.w.LAMP_2__7sec.mp4";
    videoFile = "/home/altar/repos/allip/sandbox/loop/D01.HAND.w.LAMP__HAND.and.WHITE_short.mp4";

    myMovie = new Movie(this, videoFile);
    myMovie.loop();
    background(135, 206, 235);// BLUE (0, 0, 255);
}

void draw() {
    background(135, 206, 235);// BLUE (0, 0, 255);
    
    // image(myMovie, 0, 0, width, height);

    int lm_015_x = 500;
    int lm_015_y = 368;
    
    // Display the upper half of the video without scaling
    image(myMovie, lm_015_x, lm_015_y, 96, 96, 0, 0, 96, 96);
}

void movieEvent(Movie m) {
    m.read();
}
