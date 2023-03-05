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
#ifndef __SERIAL_H__
#define __SERIAL_H__
#include "Wire.h"
void serial_sent_data(String val1, String val2, String val3, String val4, String val5, String val6, String val7)
{
  Serial.print(val1);
  Serial.print(",");
  Serial.print(val2);
  Serial.print(",");
  Serial.print(val3);
  Serial.print(",");
  Serial.print(val4);
  Serial.print(",");
  Serial.print(val5);
  Serial.print(",");
  Serial.print(val6);
  Serial.print(",");
  Serial.print(val7);
  Serial.println(",");
}
#endif
