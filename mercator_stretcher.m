% mercator_stretcher.m
% 
% Convert cylindrical projections to mercator projections
% 
% XDGFX, 2020

% --- Variables
source_file = "GRAY_HR_SR_W.tif";
target_file = "GRAY_HR_SR_W_STRETCH.tif";

index = 2;
multiplier = 2;

% --- Main Script
X = imread(source_file);
imshow(X)

% Split into top and bottom
X_top = X(1:end/2, :);
X_bottom = X(end/2+1:end, :);

% Flip bottom image
X_bottom = flipud(X_bottom);

% Initialise parameters
scale = size(X_top, 1);
width = size(X_top, 2);

input_array = linspace(0, 1, scale * multiplier);
output_array = multiplier .* input_array .^ index;

plot(input_array, output_array)

i = 1:round(scale * multiplier);

input_values = round(scale .* output_array(i) ./ multiplier);

% Remove zero values
input_values(input_values == 0) = 1;  

% Output matrix
X_top_out = X_top(input_values, :);
X_bottom_out = X_bottom(input_values, :);

% Flip bottom image back
X_bottom_out = flipud(X_bottom_out);

X_out = [X_top_out; X_bottom_out];

imwrite(X_out, target_file)