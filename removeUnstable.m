function data_stable = removeUnstable(data_interp)

% To retain the most stable features find the maximum distance (rounded to 
% the nearest pixel) traveled by each point between consecutive frames and 
% discard points with a distance exceeding the mode of the distribution.

maxVal = zeros(size(data_interp,1), 1);
%Y = diff(X) calculates differences between adjacent elements of X along the first array dimension whose size does not equal 1:

%If X is a vector of length m, then Y = diff(X) returns a vector of length m-1. The elements of Y are the differences between adjacent elements of X.

%Y = [X(2)-X(1) X(3)-X(2) ... X(m)-X(m-1)]
% May be rounded up to nearest pixel
for i = 1:size(data_interp,1)
    dif = abs(diff((data_interp(i,:))));
    maxVal(i) = max(dif);
end

avg = mean(maxVal);

% Remove those feature points whose maxVal > avg
for i = 1:size(data_interp,1)
    if maxVal(i) > avg
        data_interp(i,:) = 0;
    end
end

data_interp(all(data_interp == 0, 2),:)= [];
size(data_interp,1);
data_stable = data_interp;
end
