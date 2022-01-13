//-----------------------------------------------------------------------------------------
// Plot a line between the to points on the paper
//-----------------------------------------------------------------------------------------

void plotLine( int x1, int y1, int x2, int y2 )
{
     plotClearDisplay("plotLine");
     displayTextLine( 1,"Point 1:%d/%d", x1,y1 );
     displayTextLine( 2,"Point 2:%d/%d", x2,y2 );

     plotMoveTo( x1,y1 );
     plotPenDown();
     plotLineTo( x2,y2 );
     plotPenUp();
}

//-----------------------------------------------------------------------------------------
// Plot a rectangle with two oposite points on the paper
//-----------------------------------------------------------------------------------------

void plotRectangle( int x1, int y1, int x2, int y2 )
{
     plotClearDisplay("plotRectangle");
     displayTextLine( 1,"Point 1:%d/%d", x1,y1 );
     displayTextLine( 2,"Point 2:%d/%d", x2,y2 );

     plotMoveTo( x1,y1 );
     plotPenDown();
     plotMoveTo( x1,y2 );
     plotMoveTo( x2,y2 );
     plotMoveTo( x2,y1 );
     plotMoveTo( x1,y1 );
     plotPenUp();
}

//-----------------------------------------------------------------------------------------
// Plot a triangle with given 3 points on paper
//-----------------------------------------------------------------------------------------

void plotTriangle( int x1, int y1, int x2, int y2, int x3, int y3 )
{
     plotClearDisplay("plotTriangle");
     displayTextLine( 1,"Point 1:%d/%d", x1,y1 );
     displayTextLine( 2,"Point 2:%d/%d", x2,y2 );
     displayTextLine( 3,"Point 3:%d/%d", x3,y3 );

     plotMoveTo( x1,y1 );
     plotPenDown();
     plotLineTo( x2,y2 );
     plotLineTo( x3,y3 );
     plotLineTo( x1,y1 );
     plotPenUp();
}


//-----------------------------------------------------------------------------------------
// Plot a n edge at given position with given radius, count of edges and start angle
//-----------------------------------------------------------------------------------------

void plotNEdge( int x, int y, int radius, int edges, int start_angle )
{
     float angle;
     float delta;

     plotClearDisplay("plotNEdge");
     displayTextLine( 1,"Center:%d/%d",       x,y           );
     displayTextLine( 2,"Radius:%d Edges:%d", radius, edges );
     displayTextLine( 3,"Start-Angle:%d",     start_angle   );

     angle = start_angle;
     delta = 360/edges;

     plotMoveTo( x+radius*cos( PI/180*angle ),
                 y+radius*sin( PI/180*angle ) );

     plotPenDown();


     while( edges > 0 )
     {
            angle = angle + delta;

            plotLineTo( x+radius*cos(PI/180*angle),
                        y+radius*sin(PI/180*angle)  );

            edges--;
     }
     plotMoveTo( x+radius*cos( PI/180*angle ),
                 y+radius*sin( PI/180*angle ) );

     plotPenUp();
}


//-----------------------------------------------------------------------------------------
// Plot a circle at given position with given radius
//-----------------------------------------------------------------------------------------

void plotCircle( int x, int y, int radius )
{
     float angle;
     float delta;

     plotClearDisplay("plotCircle");
     displayTextLine( 1,"Center:%d/%d", x,y    );
     displayTextLine( 2,"Radius:%d",    radius );

     plotMoveTo( x+radius, y );

     plotPenDown();

     angle=0.0;
     delta=360/(2*radius*PI/3);

     while( angle <= 360 )
     {
            plotMoveTo( x+radius*cos(PI/180*angle),
                        y+radius*sin(PI/180*angle)  );

            angle = angle + delta;
     }
     plotMoveTo( x+radius, y );

     plotPenUp();
}
