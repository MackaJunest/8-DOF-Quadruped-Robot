/*
  Copyright © 2022 MackaJunest
  Permission is hereby granted, free of charge, to any person obtaining a copy of
  this software and associated documentation files (the “Software”), to deal in
  the Software without restriction, including without limitation the rights to
  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
  of the Software, and to permit persons to whom the Software is furnished to do
  so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in all
  copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
  SOFTWARE.
**************************************************************************************

                 Front
                 ____
           Leg1 |    |Leg2
     left       |    |       right
                |    |
           Leg4  ---- Leg3
                 Back
    H=ham
    S=shank

    L1H ____
    L1S     LEG1

    L2H ____
    L2S     LEG2

    L3H ____
    L3S     LEG3

    L4H ____
    L4S     LEG4
*/
#ifndef __SETUP_H__
#define __SETUP_H__
#include <Servo.h>

long int motion[8];
int shank1, shank2, shank3, shank4, ham1, ham2, ham3, ham4;

Servo L1H;
Servo L1S;
Servo L2H;
Servo L2S;
Servo L3H;
Servo L3S;
Servo L4H;
Servo L4S;

void Init()
{
  L1H.write(35 / 1.5);// "/1.5" for 270 degree servo
  L1S.write(100 / 1.5);

  L2H.write(35 / 1.5);
  L2S.write(100 / 1.5);

  L3H.write(35 / 1.5);
  L3S.write(100 / 1.5);

  L4H.write(35 / 1.5);
  L4S.write(100 / 1.5);
}

void setup()
{
  Serial.begin(115200);
  Serial.setTimeout(5);
  L1H.attach(2);
  L1S.attach(3);
  L2H.attach(4);
  L2S.attach(5);
  L3H.attach(6);
  L3S.attach(7);
  L4H.attach(8);
  L4S.attach(9);

  Init();

}
#endif
