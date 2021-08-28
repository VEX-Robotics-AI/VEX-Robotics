#define FONT_DIRECTION_LR     0
#define FONT_DIRECTION_BT    90
#define FONT_DIRECTION_RL   180
#define FONT_DIRECTION_TB   270



//-----------------------------------------------------------------------------------------
// Calculate the new postion px/py with delta dx/dy by taking care the direction
//-----------------------------------------------------------------------------------------

void plotCalcNewPosition( int &px, int &py, int direction, int dx, int dy )
{
     switch( direction )
     {
             case FONT_DIRECTION_LR : px = px + dx;
                                      py = py + dy;
                                      break;

             case FONT_DIRECTION_RL : px = px - dx;
                                      py = py - dy;
                                      break;

             case FONT_DIRECTION_TB : px = px + dy;
                                      py = py - dx;
                                      break;

             case FONT_DIRECTION_BT : px = px - dy;
                                      py = py + dx;
                                      break;
     }
}

//-----------------------------------------------------------------------------------------
// Give back the drawing instructions (pattern) and length of pattern (pattern_length)
// for a given letter c
//-----------------------------------------------------------------------------------------

char    *pattern;
int     pattern_length;

void GetPattern( char c )
{
     switch( c )
     {
          case '\001': pattern = "U66D6666669988888774448921444112222233U887D33666699442484424844U899D9443U66D1667U66D9443U333332\000";
                       break;
          case '\002': pattern = "D88889993332222444444U6666666\000";
                       break;
          case '\003': pattern = "8D8624U36\000";
                       break;
          case ' '   : pattern = "66666\000";
                       break;
          case '!'   : pattern = "888899D2222U22DU666\000";
                       break;
          case '"'   : pattern = "888889D2U6D8U333222\000";
                       break;
          case '#'   : pattern = "6D888888U66D222222U98D4444U88D6666U2223\000";
                       break;
          case '$'   : pattern = "8D36698744789663U77D22222222U966\000";
                       break;
          case '%'   : pattern = "D899998U444D1397U33322D1793U3\000";
                       break;
          case '&'   : pattern = "6699D114789987123333U6\000";
                       break;
          case '\''  : pattern = "888899D2U33322\000";
                       break;
          case '('   : pattern = "666D47888896U332222\000";
                       break;
          case ')'   : pattern = "6D69888874U333322\000";
                       break;
          case '*'   : pattern = "89D99U22D77U2D66U1D88U3332\000";
                       break;
          case '+'   : pattern = "99D882466U332\000";
                       break;
          case ','   : pattern = "96D21U9666\000";
                       break;
          case '-'   : pattern = "889D66U332\000";
                       break;
          case '.'   : pattern = "66DU666\000";
                       break;
          case '/'   : pattern = "D899998U222223\000";
                       break;
          case '0'   : pattern = "8D88889663222214479999U32222\000";
                       break;
          case '1'   : pattern = "8889D99222222U66\000";
                       break;
          case '2'   : pattern = "88888D9663211116666U6\000";
                       break;
          case '3'   : pattern = "88888D96632146321447U36666\000";
                       break;
          case '4'   : pattern = "666D88888811126666U32\000";
                       break;
          case '5'   : pattern = "8D3669874448886666U322222\000";
                       break;
          case '6'   : pattern = "88D96632144788889663U32222\000";
                       break;
          case '7'   : pattern = "888888D6666211222U666\000";
                       break;
          case '8'   : pattern = "8D89669874412366321447U36666\000";
                       break;
          case '9'   : pattern = "8D36698888744123669U3222\000";
                       break;
          case ':'   : pattern = "8899DU22DU336\000";
                       break;
          case ';'   : pattern = "99DU2D21U9666\000";
                       break;
          case '<'   : pattern = "669D7799U33222\000";
                       break;
          case '='   : pattern = "89D66U8D44U3336\000";
                       break;
          case '>'   : pattern = "9D9977U33332\000";
                       break;
          case '?'   : pattern = "8888D896632112U2DU666\000";
                       break;
          case '@'   : pattern = "99D79316987441223666U3\000";
                       break;
          case 'A'   : pattern = "D888889663222228884444U33366\000";
                       break;
          case 'B'   : pattern = "D888888666321444666321444U66666\000";
                       break;
          case 'C'   : pattern = "6669D144788889663U22223\000";
                       break;
          case 'D'   : pattern = "D888888666322221444U66666\000";
                       break;
          case 'E'   : pattern = "6666D444488866448886666U222223\000";
                       break;
          case 'F'   : pattern = "D88866448886666U222223\000";
                       break;
          case 'G'   : pattern = "899D6622144788889663U32222\000";
                       break;
          case 'H'   : pattern = "D8888882226666888222222U6\000";
                       break;
          case 'I'   : pattern = "6D664888888466U222233\000";
                       break;
          case 'J'   : pattern = "8D3669888884444U333332\000";
                       break;
          case 'K'   : pattern = "D88888822229999111333U6\000";
                       break;
          case 'L'   : pattern = "888888D2222226666U6\000";
                       break;
          case 'M'   : pattern = "D8888883399222222U6\000";
                       break;
          case 'N'   : pattern = "D888888233332888888U222223\000";
                       break;
          case 'O'   : pattern = "8D8888966322221447U36666\000";
                       break;
          case 'P'   : pattern = "D888888666321444U33366\000";
                       break;
          case 'Q'   : pattern = "8D888896632221147U96D33U6\000";
                       break;
          case 'R'   : pattern = "D8888886663214446333U6\000";
                       break;
          case 'S'   : pattern = "8D36698744789663U32222\000";
                       break;
          case 'T'   : pattern = "66D888888446666U222223\000";
                       break;
          case 'U'   : pattern = "888888D22222366988888U222223\000";
                       break;
          case 'V'   : pattern = "888888D222233998888U322222\000";
                       break;
          case 'W'   : pattern = "888888D2222229933888888U222223\000";
                       break;
          case 'X'   : pattern = "D899998U4444D233332U6\000";
                       break;
          case 'Y'   : pattern = "888888D223322889988U222223\000";
                       break;
          case 'Z'   : pattern = "888888D66662111126666U6\000";
                       break;
          case '['   : pattern = "666D4488888866U332222\000";
                       break;
          case '\\'  : pattern = "888888D233332U6\000";
                       break;
          case ']'   : pattern = "6D6688888844U333322\000";
                       break;
          case '^'   : pattern = "88889D93U33222\000";
                       break;
          case '_'   : pattern = "D6666U6\000";
                       break;
          case '`'   : pattern = "888889D3U33322\000";
                       break;
          case 'a'   : pattern = "669D147889662222U6\000";
                       break;
          case 'b'   : pattern = "D8889632214788888U333322\000";
                       break;
          case 'c'   : pattern = "999D74122369U3\000";
                       break;
          case 'd'   : pattern = "669D14788963888222222U6\000";
                       break;
          case 'e'   : pattern = "88D666874122366U6\000";
                       break;
          case 'f'   : pattern = "D88888963U114D66U332\000";
                       break;
          case 'g'   : pattern = "2D66988874122369U3\000";
                       break;
          case 'h'   : pattern = "D88888822663222U6\000";
                       break;
          case 'i'   : pattern = "D8888U88DU322222\000";
                       break;
          case 'j'   : pattern = "2D98888U88DU322222\000";
                       break;
          case 'k'   : pattern = "D888888U336D117333U6\000";
                       break;
          case 'l'   : pattern = "888888D222223U6\000";
                       break;
          case 'm'   : pattern = "D888829322288893222U6\000";
                       break;
          case 'n'   : pattern = "D88882963222U6\000";
                       break;
          case 'o'   : pattern = "669D1478896322U3\000";
                       break;
          case 'p'   : pattern = "2D8888866322144U6666\000";
                       break;
          case 'q'   : pattern = "666D4478896622222U9\000";
                       break;
          case 'r'   : pattern = "D8888296U3222\000";
                       break;
          case 's'   : pattern = "8D369747963U322\000";
                       break;
          case 't'   : pattern = "6D88888822466U3222\000";
                       break;
          case 'u'   : pattern = "8888D2223698882222U6\000";
                       break;
          case 'v'   : pattern = "8888D22339988U3222\000";
                       break;
          case 'w'   : pattern = "8888D222299338888U2223\000";
                       break;
          case 'x'   : pattern = "D9999U4444D3333U6\000";
                       break;
          case 'y'   : pattern = "2D6698888222147888U3333\000";
                       break;
          case 'z'   : pattern = "8888D6661112666U6\000";
                       break;
          case '{'   : pattern = "66D787989U322222\000";
                       break;
          case '|'   : pattern = "D888888U222223\000";
                       break;
          case '}'   : pattern = "D989787U333222\000";
                       break;
          case '~'   : pattern = "88888D939U322222\000";
                       break;
          case '€'   : pattern = "9666D1478888963U1D444U2D666U332\000";
                       break;
          case '¦'   : pattern = "D66666666668444444444486666666666844444444448666666666684444444444866666666668444444444486666666666U32222222\000";
                       break;
          case '§'   : pattern = "D66666666668444444444486666666666844444444448666666666684444444444866666666668444444444486666666666U32222222\000";
                       break;
          case '®'   : pattern = "8D8888966322221447U9D698742222863U36\000";
                       break;
          case '³'   : pattern = "888888D624624U3322\000";
                       break;
          default  : pattern = "\0";
     }

     pattern_length = 0;
     while( pattern[pattern_length] != '\0' )
            pattern_length++;
}

//-----------------------------------------------------------------------------------------
// Plot text on given position x/y with given size (size) in given direction (direction).
//-----------------------------------------------------------------------------------------

void plotText( int px, int py, int size, int direction, char *t )
{
     int p;
     int c;

     plotClearDisplay("plotText");
     displayTextLine( 1,"Info:%d/%d/%d/%d", px,py,size,direction );
     displayTextLine( 2,"Text:%s",          t                    );

     plotMoveTo( px,py );

     p=0;
     while( t[p] != '\0' )
     {
          GetPattern( t[p] );

          displayTextLine( 3, " /%1c :%s", t[p],pattern );

          c=0;
          while( c < pattern_length )
          {
               displayStringAt( 0,20, "%1c", pattern[c] );

               switch( pattern[c] )
               {
                  case '1' : while( pattern[c] == '1' )
                             {
                                    plotCalcNewPosition( px, py, direction, -size, -size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '2' : while( pattern[c] == '2' )
                             {
                                    plotCalcNewPosition( px, py, direction, 0, -size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '3' : while( pattern[c] == '3' )
                             {
                                    plotCalcNewPosition( px, py, direction, size, -size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '4' : while( pattern[c] == '4' )
                             {
                                    plotCalcNewPosition( px, py, direction, -size, 0 );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '6' : while( pattern[c] == '6' )
                             {
                                    plotCalcNewPosition( px, py, direction, size, 0 );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '7' : while( pattern[c] == '7' )
                             {
                                    plotCalcNewPosition( px, py, direction, -size, size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '8' : while( pattern[c] == '8' )
                             {
                                    plotCalcNewPosition( px, py, direction, 0, size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case '9' : while( pattern[c] == '9' )
                             {
                                    plotCalcNewPosition( px, py, direction, size, size );
                                    c++;
                             }
                             plotMoveTo( px,py );
                             break;

                  case 'U' : plotPenUp();
                             c++;
                             break;

                  case 'D' : plotPenDown();
                             c++;
                             break;

                  default  : c++;
               }
          }

          p++;
     }
}
