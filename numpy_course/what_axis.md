In short,

1D array: x

2D array: x, y

3D array: x, y, z

4D array: x, y, z, t

5D array: x, y, z, t, h

1D array: [ ]

2D array: [ [] , [] ]

...

Do not think of it like the above. Instead, it works more like this:
| | 0 | 1 | 2 | 4 | 5 |
|------------|------|------|------|------|------|
| 1D Indexes | Row | | | | |
| 2D Indexes | Col | Row | | | |
| 3D Indexes | Dep | Col | Row | | |
| 4D Indexes | Time | Dep | Col | Row | |
| 5D Indexes | Hist | Time | Dep | Col | Row | |

Note that this is sort of like (y, x), (z, y, x)...
If you think it like (row, col), you'll be quite tripped up by higher dimensions, where it would appear as though the pattern is nonsensically

0, 2, 1

or

0, 1, 3, 2

You can think of a three dimensional cube for 3D.

If measurements of the state of that cube were taken at different time points, we'd have data like:

(time, z, y, x)

This makes, literally, a vector of cube values. At one moment it is (z, y, x), at the next moment it has become (z+1, y+2, x-10). Moving forward in the indexes across this 'time' (4th dimension) axis, we could arrange the values across time. Note that in this analogy z, y, and x are positional dimensions, where modulating the value of, say, x, is measuring some same kind of thing (e.g. temperature in a square room at different spots).

Otherwise, a single measurement of some thing would not be a different axis from other _unrelated_ measurements. For instance, we could model temperature, windspeed, humidity, and pressure, all in one dimension as [23, 10, .6, 25]. In this case, across-time measurements could be stored as a 2-dimensional matrix.

Alternatively, you could measure these same 4 variables in two different ways each, providing a 2-dimensional matrix at each time-point, making time your 3rd dimension.

Now, if we return to the cube analogy, where positions give us three axes right at the get-go, we can add time, a series of cube states, then add something like "histories", a collection of time vectors. This might apply if we run a 20-minute experiment multiple times. Then, time gives us the state of the temperatures in a room at a certain time, while "history" determines which 20-minute _trial_ we're concerned with.

Batch together these trials, and you have another dimension above that, which would be your 6th.

In more general terms, the chart can be re-written like so:

|            | 0      | 1      | 2      | 4      | 5      | 6     |
| ---------- | ------ | ------ | ------ | ------ | ------ | ----- |
| 1D Indexes | First  |        |        |        |        |       |
| 2D Indexes | Second | First  |        |        |        |       |
| 3D Indexes | Third  | Second | First  |        |        |       |
| 4D Indexes | Fourth | Third  | Second | First  |        |       |
| 5D Indexes | Fifth  | Fourth | Third  | Second | First  |       |
| 6D Indexes | Sixth  | Fifth  | Fourth | Third  | Second | First |

Where "sixth" means your outermost abstraction, a set of fifths. just as a column is made up of many rows, and a cube of many matrices.
