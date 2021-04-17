
# heart-beat-signal-from-facial-video-for-biometric-recognition
This is project based on computer vision. In this project we have used heartbeat signals extracted from facial video for biometric detection.
# Abstract
The biometric system plays an important role in network security issues. Instead of using
a password for access control, biometric identification can be used for authentication. Biometric
information is hard to be duplicated, lost, forgotten, shared, or transferred because
it is a part of the human body. The utilization of Heartbeat Signals for biometric identification
represents a novel approach in the area of secure authentication. When blood is
pumped by the heart, some electrical and acoustic changes occur in and around the heart in
the body, which is known as a heartbeat signal. It can be accomplished by estimating Heart
Rate (HR) from face videos acquired using web-cams, smart-phone cameras or surveillance
cameras, and then Remote PPG (rPPG) method can be used to estimate PPG signal. We have
extracted PPG signals based on head motions caused by tremors of blood flowing through
arteries as stated in [1]. From PPG signals we have extracted time domain and frequency domain
features. Based on these features we have built an authentication system for biometric
recognition. \
More details can be found in  [report.pdf](https://github.com/pragyaagrawal19/heart-beat-signal-from-facial-video-for-biometric-recognition/files/6328850/report.pdf)
This repository contain two parts:
 # First part: PPG signal generation from facial video
 * PPG signal generation from facial video using principle component Analysis, which is implemented in matlab and some modules in python. (main.m is base module)
   # This part contain follwing modules-
   * main.m
   * averagePulse.m
   *  cubicSplineInterp.m
   *  faceca.m
   *  Feature_selection.m
   *  featureTraking.m
   *  gtAnalysis.m
   *  optical_flow.m
   *  processData.m
   *  read_video.m
   *  removableUnstable.m
   *  roi.m
   *  slide_image.m
   *  temporalFiltering.m
   *  SignalAnalyser.py
   *  centerRows
   *  PCA
   # True_ppg_random1 is ppg signal calculated 
 # Second part: biometric recognition using facial video: 
    It is implemented in python. It contains following modules:
    * init.py
    * feature.py
    * learn.py
    * param.py
    * signal.py
    * utils.py
    *  classify.py
    * convert.py
    * extract.py
    * feature_extract.py 
    
     # result.txt shows result of our experiment.
   
    
