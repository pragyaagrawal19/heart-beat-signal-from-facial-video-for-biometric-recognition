function [forehead, nose] = roi(V)


%The cascade object detector uses the Viola-Jones algorithm to detect people’s forehead, noses.
faceDetector = vision.CascadeObjectDetector; %creating a detector
%for i = 1:numFr
 %    face = step(faceDetector, read(V,i));
  %   face = [face(1)+face(3)*0.2 face(2)+face(4)*0.05 face(3)*0.52 face(4)-face(4)*0.15];
   %  IFaces = insertObjectAnnotation(read(V,i), 'rectangle', face, '');
    % imshow(IFaces);
%end

face = step(faceDetector, read(V,1));
% face = [face(1)+face(3)*0.25 face(2) face(3)*0.5 face(4)-face(4)*0.10];
% forehead = [face(1) face(2) face(3) face(4)*0.2];
% nose = [face(1) face(2)+face(4)*0.55 face(3) face(4)*0.45];

% New
face = [face(1)+face(3)*0.25 face(2) face(3)*0.5 face(4)-face(4)*0.10];
forehead = [face(1) face(2) face(3) face(4)*0.25];
nose = [face(1) face(2)+face(4)*0.55 face(3) face(4)*0.45];

%IFaces = insertObjectAnnotation(read(V,1), 'rectangle', [forehead; nose], '');
 % imshow(IFaces);
end



