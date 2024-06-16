import processing.video.*;

int time;
Movie myMovie;
int locx = 0;
int locy = 0;

// Variables for the videos folder
String homeDir = System.getProperty("user.home");
String videosFolderMac = homeDir + "/Documents/works.and.docs/2024.amot/pawns.court/altar.aleph/exports/";
String videosFolderPi = homeDir + "/pawns.court/altar.aleph/exports/";
String videosFolder;

void setup() {
    printArgs("setup");
    
    if (isDry()) {
        return;
    }
    
    defineVideosFolder();
    println("OS := " + System.getProperty("os.name"));
    println("videos folder := " + videosFolder);
    String videoFileName = "D01.HAND.w.LAMP_2.mp4";
    String videoFile = videosFolder + videoFileName;
    println("video file := " + videoFile);
    
    // Check if the video file exists
    if (!isValidFile(videoFile)) {
        println("Error: The video file does not exist or is not accessible.");
        return;
    }
    
    // Set a windowed size for development
    size(800, 600, P2D);
    
    
    // Load the 96x192 video file
    myMovie = new Movie(this, videoFile);
    if (myMovie.width != 92 && myMovie.height != myMovie.width * 2) {
        //TODO: make code robust to video size
        println("video size is wrong: " + " width = " + myMovie.width + " height = " + myMovie.height);
        println("quiting...");
        return;
    }
    myMovie.loop(); // Start looping the video
    background(135, 206, 235);// BLUE (0, 0, 255);
    time = millis();
}

void draw() {
    if (isDry()) {
        return;
    }
    
    background(135, 206, 235);// BLUE (0, 0, 255);

    //TODO: this is not clear    
    // if (myMovie.available() == true) {
    //     myMovie.read(); // Read new frame
    // }
    
    // := image(myMovie, x, y, width, height, srcX, srcY, srcWidth, srcHeight)
    
    if (isDebug()) {
        image(myMovie, 110, 0); // play entire image
    }
    
    if (isCalib()) {
        if ((millis() - time) > 800) {
            time = millis();
            locx = locx + 50;
            println("calib curr (x, y) = (" + locx + ", " + locy + ")");
            if (locx > (800 - 96)) {
                locx = 0;
                locy = locy + 50;
            } 
            if (locy > (600 - 96)) {
                locy = 0;
            }
        }
        // Display the upper half of the video without scaling
        image(myMovie, locx, locy, 96, 96, 0, 0, 96, 96);
    } else {
        int lm_015_x = 500;
        int lm_015_y = 368;
        
        // Display the upper half of the video without scaling
        image(myMovie, lm_015_x, lm_015_y, 96, 96, 0, 0, 96, 96);

        int lm_182_x = 596;
        int lm_182_y = 176;

        // Display the lower half of the video without scaling
        image(myMovie, lm_182_x, lm_182_y, 96, 96, 0, 96, 96, 192);
    }
}

// Called every time a new frame is available to read
void movieEvent(Movie m) {
    m.read();
}


/* HELPERS */

void printArgs(String from) {
println();
println("Arguments from " + from + ":");
if (args != null && args.length > 0) {
for (int i = 0; i < args.length; i++) {
println(String.format("  Argument %d: %s", i, args[i]));
}
    } else {
println("  No arguments passed.");
    }
println();
}

// Function to check if there are any command-line arguments
boolean hasArgs() {
return args != null && args.length > 0;
}

// Function to check if a specific argument at an index equals a value
boolean hasArgs(int index, String value) {
// `0` args[0] = `--args`
if(args != null && index >= 0 && index < args.length) {
return args[index].equals(value);
    }
return false;
}

boolean argsHasValue(String value) {
boolean res = false;
if (args != null && args.length > 0) {
for (int i = 0; i < args.length; i++) {
if (args[i].toLowerCase().equals(value)) {
res = true;
break;
}
}
    }
return res;
}

boolean isDry() { 
boolean res = argsHasValue("dry");
return res;
}

boolean isDebug() { 
boolean res = argsHasValue("debug");
return res;
}

boolean isCalib() {
boolean res = argsHasValue("calib");
return res;
}

//Detect the operating system and set the folder path accordingly
void defineVideosFolder() {
if (System.getProperty("os.name").toLowerCase().contains("mac")) {
videosFolder = videosFolderMac;
    } else if (System.getProperty("os.name").toLowerCase().contains("linux")) {
videosFolder = videosFolderPi;
    }
}

// Function to check if a path points to a valid file
boolean isValidFile(String filePath) {
File file = new File(filePath);
return file.exists() && file.isFile();
}
