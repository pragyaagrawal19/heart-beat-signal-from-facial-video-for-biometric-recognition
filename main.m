% Videos
A=['A';'D';'E';'F';'G';'H';'I';'J';'K';'L';'M';'N';'B'];
l=[4;8;4;4;5;4;4;8;8;7;8;8;7;8];
j=2;
X=l(j,1);
for i=1:l(j,1)
     disp(strcat(A(j,1),'(',num2str(i),')'));
     video=strcat('/data/bonafide/',A(j,1), ' (',num2str(i),')','.avi');
     V= VideoReader(video);

frameRate = V.FrameRate;
numFr = V.NumberOfFrames;

[forehead, nose] = roi(V);
% imshow(foreheadnose);
% In feature tracking we try to extract visual features like corners and
% track them over multiple frames.
[x, y] = featureTracking(V, forehead, nose);
%%imshow(insertMarker(forehead,[x(:,1) y(:,1)],'*', 'Size', 5, 'Color', 'green'));
  %s=strcat('C:\Users\pragy\Desktop\CVproject\data\xy_data',A(j,1),num2str(i),'.mat');
 %save(s,'x','y');

samplingRate = 250;

x_interp = cubicSplineInterp(V, x, samplingRate);
y_interp = cubicSplineInterp(V, y, samplingRate);
%retain most stable features
x_stable = removeUnstable(x_interp);
y_stable = removeUnstable(y_interp);
% temperol filtering beacuase we need frequency between 0.75 to 5 hz only.
x_filtered = temporalFiltering(x_stable);
y_filtered = temporalFiltering(y_stable);

%% Component Analysis Part
%addpath(genpath('ComponentAnalysis'),'ca_data');

% Perform PCA
tic
y_pca = PCA(y_filtered,5);
time_pca = toc;
break;
%save(strcat('C:\Users\pragy\Desktop\CVproject\data\',A(j,1),num2str(i),'.mat'),'y_pca','time_pca');
end
%bad component removal
A=['A';'D';'E';'F';'G';'H';'I';'J';'K';'L';'M';'N';'B'];
i=1;
for i=1:length(A)
files=dir(fullfile('C:\Users\pragy\Desktop\CVproject\data\ca_data\B',strcat(A(i,1),'*.mat')));
l=length(files);
for k=1:l
    name=files(k).name;
    FileData = load(fullfile('C:\Users\pragy\Desktop\CVproject\data\ca_data\B',name));
    Y_pca=FileData.y_pca;
for component=1:size(Y_pca,1)
  min1 = int8(min(Y_pca(component,:)));
  max1= int8(max(Y_pca(component,:)));
  overfitting_value = std(Y_pca(component,:));
  overfitting_value=int8(overfitting_value*3);
  if abs(min1 + overfitting_value)>0 | abs(max1-overfitting_value) > 0
      Y_pca(component,:)=0;
  end
end
Y_pca(all(~Y_pca,2),:)=[];
if(isempty(Y_pca) == 0)
  s=size(Y_pca,1);
  Y=randsample(s,1);
  signal=Y_pca(Y,:);
end
person=i;
video_no=k;
x=[person,video_no,signal];
%dlmwrite('ppg_random.csv',x,'-append');
end
end




































