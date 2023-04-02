from keras.models import load_model
from time import sleep
from keras.utils import img_to_array
from keras.preprocessing import image
import cv2
import numpy as np
import streamlit as st
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase, RTCConfiguration, VideoProcessorBase, WebRtcMode

st.title("Facial Expression Emotion Recognition")
st.header("Webcam Live Feed")
st.write("Click on start to use webcam and detect your face emotion")
webrtc_streamer(key="example", mode=WebRtcMode.SENDRECV, rtc_configuration=RTC_CONFIGURATION,video_processor_factory=Faceemotion)