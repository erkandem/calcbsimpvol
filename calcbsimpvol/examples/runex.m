% This is MATLAB script to run similiar examples in both MATLAB and Python
% The Examples are derived from the original MATLAB .m-code distribution of the function/package
% Having said that, this file is only of value if you have a both interpreters installed
% and run this particular script from within MATLAB
%
% depending on which distribution of python was installed and
% how it was installed (think of symlinks in linux dists)
% try to replace 'python' with 'python3', 'python2', 'python_xy'
% within ``system(sprintf('python %s', file_path))``

%% Example 1
root_path = pwd();
addpath(fullfile(root_path, 'calcBSImpVol_mlab'))
S = 100; K = (40:25:160)'; T = (0.25:0.25:1)'; % Define Key Variables
r = 0.01; q = 0.03;
cp = 1; % i.e. call
P = [[59.35, 34.41, 10.34, 0.50, 0.01]
    [58.71, 33.85, 10.99, 1.36, 0.14]
    [58.07, 33.35, 11.50, 2.12, 0.40]
    [57.44, 32.91, 11.90, 2.77, 0.70]];

[mK, mT] = meshgrid(K, T);
[sigma, ~] = calcBSImpVol(cp, P, S, mK, mT, r, q);
disp(sigma)

% MLB
%        NaN       NaN    0.2071    0.2182    0.2419
%        NaN    0.2228    0.2024    0.2139    0.2374
%        NaN    0.2244       NaN    0.2106    0.2345
%        NaN    0.2219    0.1956    0.2080    0.2305     


file_path = fullfile(root_path, 'example1.py');
system(sprintf('python3 %s', file_path))

% python
%[[       nan        nan 0.20709362 0.21820954 0.24188675]
% [       nan 0.22279836 0.20240934 0.21386148 0.23738982]
% [       nan 0.22442837 0.1987048  0.21063506 0.23450013]
% [       nan 0.22188111 0.19564657 0.20798285 0.23045406]]

%% Example 2 
root_path = pwd();
addpath(fullfile(root_path, 'calcBSImpVol_mlab'))

S = 100; K = (40:25:160)'; T = (0.25:0.25:1)'; % Define Key Variables
cp = [ones(4, 3),-ones(4, 2)]; % [Calls[4, 3], Puts[4, 2]]
R = 0.01 * repmat([1.15; 1.10; 1.05; 1], 1, 5); % 
Q = 0.03 * repmat([1.3; 1.2; 1.1; 1], 1, 5);
P = [[59.14, 34.21, 10.17, 16.12, 40.58]
    [58.43, 33.59, 10.79, 17.47, 41.15]
    [57.87, 33.16, 11.363, 18.63, 41.74]
    [57.44, 32.91, 11.90, 19.58, 42.27]];
[mK, mT] = meshgrid(K,T);
[sigma, ~] = calcBSImpVol(cp, P, S, mK, mT, R, Q);
disp(sigma)

% MLB
%        NaN       NaN    0.2063    0.2181    0.2467
%        NaN    0.2257    0.2021    0.2139    0.2373
%     0.2952    0.2256    0.1987    0.2110    0.2348
%        NaN    0.2219    0.1956    0.2079    0.2310


file_path = fullfile(root_path, 'example2.py');
system(sprintf('python3 %s', file_path))

% python
%[[       nan        nan 0.20632041 0.21805647 0.24672859]
% [       nan 0.22571652 0.20213163 0.21393441 0.23734226]
% [0.29522239 0.22556393 0.19872376 0.21099555 0.23484719]
% [       nan 0.22188111 0.19564657 0.20794493 0.23099783]]
