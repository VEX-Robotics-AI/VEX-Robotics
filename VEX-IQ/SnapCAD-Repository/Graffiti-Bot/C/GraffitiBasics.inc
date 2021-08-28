//---------------------------------------------------------------------------------------------------------
// Define global constants
//---------------------------------------------------------------------------------------------------------

#define PLOT_SPEED           50

#define X_SIZE             2250
#define Y_SIZE             2150

#define MIN_X_VALUE     -X_SIZE
#define MAX_Y_VALUE      Y_SIZE
#define MAX_X_VALUE           0
#define MIN_Y_VALUE           0

#define PEN_UP             true
#define PEN_DOWN          false


//---------------------------------------------------------------------------------------------------------
//  Define global variables
//---------------------------------------------------------------------------------------------------------

int     motorx_lastpos;         // Internal value of last position of x axis
int     motory_lastpos;         // Internal value of last position of y axis

int     border_right;           // right border of physical drawing area
int     border_left;            // left border of physical drawing area
int     border_bottom;          // bottom border of physical drawing area
int     border_top;             // top border of physical drawing area

bool    pen_position_z;         // Internal value of position of the pen
int     pen_position_x;         // current position of the pen on the paper
int     pen_position_y;         // current position of the pen on the paper


//---------------------------------------------------------------------------------------------------------
// Task Display plotter status (~ 10 time per second)
//---------------------------------------------------------------------------------------------------------

task taskDisplayCurrentStatus()
{
     while( true )
     {
          pen_position_x = getMotorEncoder( MotorX ) + X_SIZE;
          pen_position_y = getMotorEncoder( MotorY );

          displayInverseStringAt(  7,8,"%5d", pen_position_x );
          displayInverseStringAt( 49,8,"%5d", pen_position_y );

          if( pen_position_z == PEN_UP )
              displayInverseStringAt( 104,8, " up " );
          else
              displayInverseStringAt( 104,8, "down" );

          sleep( 100 );
     }
}


//---------------------------------------------------------------------------------------------------------
// Erase field for information (line0 - line4 )
//---------------------------------------------------------------------------------------------------------

void plotClearDisplay( char *info )
{
     eraseRect( 0,47,127,11 );
     fillRect( 0,47,127,37 );
     displayInverseStringAt(0,44,info );
}


//---------------------------------------------------------------------------------------------------------
// Check for defined borders and correct value if necessary
//---------------------------------------------------------------------------------------------------------

void plotCheckForBorders( int &x, int &y )
{
     if( x < border_left )
         x = border_left;
     if( x > border_right )
         x = border_right;
     if( y < border_bottom )
         y = border_bottom;
     if( y > border_top )
         y = border_top;
}


//---------------------------------------------------------------------------------------------------------
// Move the pen up
//---------------------------------------------------------------------------------------------------------

void plotPenUp()
{
     pen_position_z = PEN_UP;

     setMotorTarget( MotorPen, getMotorEncoder( MotorPen )-260, 100 );
     waitUntilMotorStop( MotorPen );
}


//---------------------------------------------------------------------------------------------------------
// Move the pen down
//---------------------------------------------------------------------------------------------------------

void plotPenDown()
{
     pen_position_z = PEN_DOWN;

     setMotorTarget( MotorPen, getMotorEncoder( MotorPen )+220, 100 );
     waitUntilMotorStop( MotorPen );
}


//---------------------------------------------------------------------------------------------------------
// Move to the home position
//---------------------------------------------------------------------------------------------------------

void plotMoveHome()
{
     plotClearDisplay( "Home position" );

     setMotorTarget( MotorX, 0, PLOT_SPEED );
     setMotorTarget( MotorY, 0, PLOT_SPEED );

     waitUntilMotorStop( MotorX );
     waitUntilMotorStop( MotorY );
}


//---------------------------------------------------------------------------------------------------------
// Move the pen to the given position
//---------------------------------------------------------------------------------------------------------

void plotMoveTo( int px, int py )
{
     plotCheckForBorders( px,py );

     setMotorTarget( MotorX, px+MIN_X_VALUE, PLOT_SPEED );
     setMotorTarget( MotorY, py,             PLOT_SPEED );

     waitUntilMotorStop( MotorX );
     waitUntilMotorStop( MotorY );

     motorx_lastpos = px;
     motory_lastpos = py;
}


//---------------------------------------------------------------------------------------------------------
// Move the pen to the given position by using small steps (if necessary)
//---------------------------------------------------------------------------------------------------------

void plotLineTo( int x2, int y2 )
{
     float l;
     float i;
     int   x1;
     int   y1;

     x1 = motorx_lastpos;
     y1 = motory_lastpos;

     if( ( x1 == x2 ) ||
         ( y1 == y2 )    )
     {
         plotMoveTo( x2, y2 );
     }
     else
     {
         l = sqrt( (x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));

         i=0;
         while( i < l )
         {
                plotMoveTo( x1+(x2-x1)/l*i,
                            y1+(y2-y1)/l*i );
                i=i+5;
         }
         plotMoveTo( x2, y2 );
     }
}


//---------------------------------------------------------------------------------------------------------
// Initialize the plotter
//---------------------------------------------------------------------------------------------------------

void plotInit()
{
    // Clear LCD

    eraseDisplay();
    displayCenteredBigTextLine( 0,"Initialize" );
    displayCenteredBigTextLine( 2,"Plotter" );

    // First lift the pen before anything else will be moved!

    plotPenUp();

    // when EndX not reached then move right until it will be reached

    if( getBumperValue( EndX ) == 0 )
    {
        setMotorSpeed( MotorX, 50 );
        while( getBumperValue( EndX ) == 0 )
	           delay(10);
        setMotorSpeed( MotorX, 0 );
    }

	  // Release end position and move back

    if( getBumperValue( EndX ) == 1 )
    {
        setMotorSpeed( MotorX, -50 );
        delay( 100 );
        setMotorSpeed( MotorX, 0 );
    }

    // Set the current position as zero position

    resetMotorEncoder( MotorX );

    // when EndX not reached then move right until it will be reached

    if( getBumperValue( EndY ) == 0 )
    {
        setMotorSpeed( MotorY, -50 );
	      while( getBumperValue( EndY ) == 0 )
	             delay(10);
	      setMotorSpeed( MotorY, 0 );
	  }

	  // Release end position and move back

	  if( getBumperValue( EndY ) == 1 )
    {
        setMotorSpeed( MotorY, 50 );
        delay( 150 );
        setMotorSpeed( MotorY, 0 );
    }

    // Set the current position as zero position

    resetMotorEncoder( MotorY );
    motorx_lastpos = 0;
    motory_lastpos = 0;

    border_left   = getMotorEncoder( MotorX );
    border_bottom = getMotorEncoder( MotorY );
    border_right  = X_SIZE;
    border_top    = Y_SIZE;

    // move to bottom right corner

    plotMoveHome();

    // Prepare display

    eraseDisplay();

    displayStringAt( 0, 8, "X"   );
    displayStringAt( 42,8, "Y"   );
    displayStringAt( 85,8, "Pen" );

    drawLine(   0,10,128,10 );
    drawLine(   6, 1,  6, 8 );
    drawLine(  48, 1, 48, 8 );
    drawLine( 103, 1,103, 8 );

    // Start background task which update the current status of the plotter

    startTask( taskDisplayCurrentStatus );
}
