import processing.video.*;
int time;
Movie myMovie; // Declare movie variable
int locx=0;
int locy=0;
void setup() {
  // fullScreen(P2D, 1);
  size(720,720);
  print(width);
  print(height);
  // Initial setup for your Processing sketch
  //size(100, 100); // Set the size of the window
  myMovie = new Movie(this, "a.mov"); // Load the video file
  myMovie.play(); // Start playing the video
  
  // Position the sketch window on a specific screen (e.g., secondary monitor)
  // You may need to adjust these values based on your screen setup
  //int sketchX = 1920; // X position (for a dual monitor setup where the primary monitor is 1920 pixels wide)
  //int sketchY = 0; // Y position
  //surface.setLocation(0, sketchY); // Set the location of the sketch window
  time=millis();
}

void draw() {
    time=millis();
//  if ((millis()-time)>400){time=millis();locx=locx+50;println('x');println(locx);println(locy);
//  if ((locx>800)){locx=0;locy=locy+50;}
//}
//  background(0);
  if (myMovie.available() == true) {
    myMovie.read(); // Read new frame
  }
  image(myMovie,0,0,480,720);
  //image(myMovie, 596,308,96,96); // A
//  //image(myMovie, locx,locy,96,96); 
//    //image(myMovie, 500,404,96,96); //B
//    image(myMovie, 596,20,96,96); //C
println(millis()-time);
}

// Called every time a new frame is available to read
void movieEvent(Movie m) {
  m.read();
}
// import java.io.File;

// void setup() {
//   String folder = "data";
//   String filename = "myfile.txt";
//   File file = new File(folder, filename);
  
//   println("Path: " + file.getPath());
//   println("Absolute Path: " + file.getAbsolutePath());
//   println("Exists: " + file.exists());
// }
