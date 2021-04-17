function varargout = featureTracking(V, forehead, nose)

nout = max(nargout,1); %Number of output variables
% detectMinEigenFeatures(I) returns a cornerPoints object, points. 
%The object contains information about the feature points detected in a
%2-D grayscale input image, I. The detectMinEigenFeatures function uses 
%the minimum eigenvalue algorithm developed by Shi and Tomasi to find feature points.
pointsF = detectMinEigenFeatures(rgb2gray(read(V,1)),'ROI',forehead);
pointsN = detectMinEigenFeatures(rgb2gray(read(V,1)),'ROI',nose);
%pointImage = insertMarker(read(V,1),[pointsF.Location; pointsN.Location],'+','Color','red');
%imshow(pointImage);
%vision.PointTracker returns a point tracker object that tracks a set of points in a video.
%using kanade-Lucus-Thomasi-algorithm
trackerF = vision.PointTracker('MaxBidirectionalError',1);
trackerN = vision.PointTracker('MaxBidirectionalError',1);
%The initial locations points, must be an M-by-2 array of [x y] coordinates. 
initialize(trackerF, pointsF.Location,read(V,1));
initialize(trackerN, pointsN.Location,read(V,1));

[pointsF, validityF] = step(trackerF,read(V,1));
[pointsN, validityN] = step(trackerN,read(V,1));

numFr = V.NumberOfFrames;

for j = 1:nout
    varargout{j} = zeros(size(pointsF,1) + size(pointsN,1), numFr);
end
% x = zeros(size(pointsF,1) + size(pointsN,1), numFr);
% y = zeros(size(pointsF,1) + size(pointsN,1), numFr);

for i = 1:numFr
    [pointsF, validityF] = step(trackerF,read(V,i));
    [pointsN, validityN] = step(trackerN,read(V,i));
    for j = 1:nout
        varargout{j}(1:size(pointsF,1),i) = pointsF(:,j);
        varargout{j}(size(pointsF,1)+1:size(pointsF,1)+size(pointsN,1),i) = pointsN(:,j);
    end
   %x(1:size(pointsF,1),i) = pointsF(:,1);
    % x(size(pointsF,1)+1:size(pointsF,1)+size(pointsN,1),i) = pointsN(:,1);
     %y(1:size(pointsF,1),i) = pointsF(:,2);
     %y(size(pointsF,1)+1:size(pointsF,1)+size(pointsN,1),i) = pointsN(:,2);
     %out = insertMarker(read(V,i),[pointsF(validityF, :); pointsN(validityN, :)],'+');
     %figure,imshow(out);
end

out = insertMarker(read(V,1),[pointsF(validityF, :); pointsN(validityN, :)],'+');
figure, imshow(out);
%size(pointsF,1)+size(pointsN,1);
end
