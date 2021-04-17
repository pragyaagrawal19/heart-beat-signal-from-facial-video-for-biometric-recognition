function data_interp = cubicSplineInterp(V, data, samplingRate)

% Increase sampling rate from frameRate to samplingRate Hz

frameRate = V.FrameRate;
numFr = V.NumberOfFrames;
% Intrerpolate out data matrix to fit sampling rate 250 hz.
% new data size F*10T
data_interp = zeros(size(data,1), round(numFr*samplingRate/frameRate));

xx = linspace(1,numFr,round(numFr*samplingRate/frameRate));
%interpolation is a type of estimation, a method of constructing new data points within the range of a discrete set of known data points.

for i = 1:size(data,1)
    data_interp(i,:) = spline(1:numFr,data(i,:),xx);
%    yinterp(i,:) = spline(1:numFr,y(i,:),xx);
 %    plot(x(i,:),y(i,:),'o',xinterp,yinterp)
end

%figure, scatter(xx, data_interp(1,:))
end




