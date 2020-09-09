'''
l = [560.7597073, 498.0334064, 565.6706018, 65.94466364, 298.0371737, 24.01104473, 226.2917231, 61.70916623, 218.7689618, 43.38005224, 149.6222347, 120.9704561, 57.50884221, 142.0531183, 186.7431199, 43.54798079, 36.02953492, 162.4225154]
for i in l:
    for j in l:
        print "%0.2f" % abs(i-j),

    print
'''

delay = [
[ 0     , 21.62 , 24.42 , 0.57  , 7.74  , 9.18  , 1.01  , 0.76  , 18.44 , 21.14 , 26.56 , 19.78 , 23.61 , 16.76 , 23.34 , 21.5  , 24.11 , 23.54 ],
[ 21.62 , 0     , 19.31 , 21.47 , 28.97 , 21.35 , 21.12 , 20.89 , 3.63  , 0.68  , 6.12  , 8.61  , 3.84  , 13.02 , 17.38 , 23.68 , 13.5  , 18.4  ],
[ 24.42 , 19.31 , 0     , 24.4  , 27.85 , 30.31 , 23.88 , 25.03 , 17.9  , 19.61 , 23.9  , 17.96 , 19.91 , 9.17  , 2.22  , 9.85  , 8.51  , 1.12  ],
[ 0.57  , 21.47 , 24.4  , 0     , 7.2   , 8.98  , 1.47  , 0.49  , 18.79 , 22.33 , 28.24 , 20.79 , 23.4  , 18.78 , 25.77 , 25.47 , 15.34 , 26.08 ],
[ 7.74  , 28.97 , 27.85 , 7.2   , 0     , 16    , 7.99  , 7.57  , 10.47 , 19.58 , 11.97 , 17.15 , 12.21 , 11.71 , 32.15 , 16.72 , 40.13 , 26.01 ],
[ 9.18  , 21.35 , 30.31 , 8.98  , 16    , 0     , 9.38  , 9.21  , 16.17 , 25.17 , 6.62  , 37.8  , 15.45 , 11.66 , 26.84 , 12.99 , 34.76 , 30.03 ],
[ 1.01  , 21.12 , 23.88 , 1.47  , 7.99  , 9.38  , 0     , 0.52  , 25.82 , 20.5  , 15.36 , 21.77 , 21.49 , 29.29 , 23.51 , 19.49 , 19.35 , 24.02 ],
[ 0.76  , 20.89 , 25.03 , 0.49  , 7.57  , 9.21  , 0.52  , 0     , 19.21 , 22.96 , 18.89 , 22.72 , 20.42 , 31.77 , 22.22 , 26.9  , 28.28 , 26.02 ],
[ 18.44 , 3.63  , 17.9  , 18.79 , 10.47 , 16.17 , 25.82 , 19.21 , 0     , 3.47  , 6.08  , 7.5   , 7.39  , 18.24 , 22.64 , 19.38 , 27.24 , 14.79 ],
[ 21.14 , 0.68  , 19.61 , 22.33 , 19.58 , 25.17 , 20.5  , 22.96 , 3.47  , 0     , 5.55  , 8.7   , 3.93  , 10.25 , 16.57 , 28.24 , 10.8  , 20.63 ],
[ 26.56 , 6.12  , 23.9  , 28.24 , 11.97 , 6.62  , 15.36 , 18.89 , 6.08  , 5.55  , 0     , 3.35  , 5.76  , 4.48  , 16.02 , 14.44 , 26.07 , 25.23 ],
[ 19.78 , 8.61  , 17.96 , 20.79 , 17.15 , 37.8  , 21.77 , 22.72 , 7.5   , 8.7   , 3.35  , 0     , 9.07  , 9.9   , 24.59 , 37.7  , 6.67  , 13.57 ],
[ 23.61 , 3.84  , 19.91 , 23.4  , 12.21 , 15.45 , 21.49 , 20.42 , 7.39  , 3.93  , 5.76  , 9.07  , 0     , 32.04 , 24.7  , 16.57 , 19.08 , 19.81 ],
[ 16.76 , 13.02 , 9.17  , 18.78 , 11.71 , 11.66 , 29.29 , 31.77 , 18.24 , 10.25 , 4.48  , 9.9   , 32.04 , 0     , 8.48  , 15.94 , 13.06 , 8.33  ],
[ 23.34 , 17.38 , 2.22  , 25.77 , 32.15 , 26.84 , 23.51 , 22.22 , 22.64 , 16.57 , 16.02 , 24.59 , 24.7  , 8.48  , 0     , 7.77  , 9.45  , 1.52  ],
[ 21.5  , 23.68 , 9.85  , 25.47 , 16.72 , 12.99 , 19.49 , 26.9  , 19.38 , 28.24 , 14.44 , 37.7  , 16.57 , 15.94 , 7.77  , 0     , 5.75  , 10.64 ],
[ 24.11 , 13.5  , 8.51  , 15.34 , 40.13 , 34.76 , 19.35 , 28.28 , 27.24 , 10.8  , 26.07 , 6.67  , 19.08 , 13.06 , 9.45  , 5.75  , 0     , 8.49  ],
[ 23.54 , 18.4  , 1.12  , 26.08 , 26.01 , 30.03 , 24.02 , 26.02 , 14.79 , 20.63 , 25.23 , 13.57 , 19.81 , 8.33  , 1.52  , 10.64 , 8.49  , 0     ]]


credit = [
[0      , 6.273  , 0.491  , 49.482 , 26.272 , 53.675 , 33.447 , 49.905 , 34.199 , 51.738 , 41.114 , 43.979 , 50.325 , 41.871 , 37.402 , 51.721 , 52.473 , 39.834 ],
[6.273  , 0      , 6.764  , 43.209 , 20     , 47.402 , 27.174 , 43.632 , 27.926 , 45.465 , 34.841 , 37.706 , 44.052 , 35.598 , 31.129 , 45.449 , 46.2   , 33.561 ],
[0.491  , 6.764  , 0      , 49.973 , 26.763 , 54.166 , 33.938 , 50.396 , 34.69  , 52.229 , 41.605 , 44.47  , 50.816 , 42.362 , 37.893 , 52.212 , 52.964 , 40.325 ],
[49.482 , 43.209 , 49.973 , 0      , 23.209 , 4.193  , 16.035 , 0.424  , 15.282 , 2.256  , 8.368  , 5.503  , 0.844  , 7.611  , 12.08  , 2.24   , 2.992  , 9.648  ],
[26.272 , 20     , 26.763 , 23.209 , 0      , 27.403 , 7.175  , 23.633 , 7.927  , 25.466 , 14.841 , 17.707 , 24.053 , 15.598 , 11.129 , 25.449 , 26.201 , 13.561 ],
[53.675 , 47.402 , 54.166 , 4.193  , 27.403 , 0      , 20.228 , 3.77   , 19.476 , 1.937  , 12.561 , 9.696  , 3.35   , 11.804 , 16.273 , 1.954  , 1.202  , 13.841 ],
[33.447 , 27.174 , 33.938 , 16.035 , 7.175  , 20.228 , 0      , 16.458 , 0.752  , 18.291 , 7.667  , 10.532 , 16.878 , 8.424  , 3.955  , 18.274 , 19.026 , 6.387  ],
[49.905 , 43.632 , 50.396 , 0.424  , 23.633 , 3.77   , 16.458 , 0      , 15.706 , 1.833  , 8.791  , 5.926  , 0.42   , 8.034  , 12.503 , 1.816  , 2.568  , 10.071 ],
[34.199 , 27.926 , 34.69  , 15.282 , 7.927  , 19.476 , 0.752  , 15.706 , 0      , 17.539 , 6.915  , 9.78   , 16.126 , 7.672  , 3.203  , 17.522 , 18.274 , 5.635  ],
[51.738 , 45.465 , 52.229 , 2.256  , 25.466 , 1.937  , 18.291 , 1.833  , 17.539 , 0      , 10.624 , 7.759  , 1.413  , 9.867  , 14.336 , 0.017  , 0.735  , 11.904 ],
[41.114 , 34.841 , 41.605 , 8.368  , 14.841 , 12.561 , 7.667  , 8.791  , 6.915  , 10.624 , 0      , 2.865  , 9.211  , 0.757  , 3.712  , 10.607 , 11.359 , 1.28   ],
[43.979 , 37.706 , 44.47  , 5.503  , 17.707 , 9.696  , 10.532 , 5.926  , 9.78   , 7.759  , 2.865  , 0      , 6.346  , 2.108  , 6.577  , 7.742  , 8.494  , 4.145  ],
[50.325 , 44.052 , 50.816 , 0.844  , 24.053 , 3.35   , 16.878 , 0.42   , 16.126 , 1.413  , 9.211  , 6.346  , 0      , 8.454  , 12.923 , 1.396  , 2.148  , 10.491 ],
[41.871 , 35.598 , 42.362 , 7.611  , 15.598 , 11.804 , 8.424  , 8.034  , 7.672  , 9.867  , 0.757  , 2.108  , 8.454  , 0      , 4.469  , 9.851  , 10.602 , 2.037  ],
[37.402 , 31.129 , 37.893 , 12.08  , 11.129 , 16.273 , 3.955  , 12.503 , 3.203  , 14.336 , 3.712  , 6.577  , 12.923 , 4.469  , 0      , 14.32  , 15.071 , 2.432  ],
[51.721 , 45.449 , 52.212 , 2.24   , 25.449 , 1.954  , 18.274 , 1.816  , 17.522 , 0.017  , 10.607 , 7.742  , 1.396  , 9.851  , 14.32  , 0      , 0.752  , 11.887 ],
[52.473 , 46.2   , 52.964 , 2.992  , 26.201 , 1.202  , 19.026 , 2.568  , 18.274 , 0.735  , 11.359 , 8.494  , 2.148  , 10.602 , 15.071 , 0.752  , 0      , 12.639 ],
[39.834 , 33.561 , 40.325 , 9.648  , 13.561 , 13.841 , 6.387  , 10.071 , 5.635  , 11.904 , 1.28   , 4.145  , 10.491 , 2.037  , 2.432  , 11.887 , 12.639 , 0      ]]


a = 0.5
b = 0.5


result = []

length = len(credit)

for i in range(length):
    temp = []
    for j in range(length):
        temp.append(round(delay[i][j] * a + credit[i][j] * b, 2))
    result.append(temp)

print result
'''
i = delay[0]
j = credit[0]
print i
print j
c = [x + y for  x, y in zip(i, j)]
print c
'''