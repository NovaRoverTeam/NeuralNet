#python /home/nvidia/catkin_ws/src/core_rover/scripts/tennis_loc.py & 
gst-launch-1.0 rtspsrc location=rtsp://nova:rovanova@192.168.1.53:88/videoMain ! decodebin ! videoscale ! video/x-raw, width=720, height=500 ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5002 sync=false & #python3 V2_Foscam_2.py && fg

#gst-launch-1.0 rtspsrc location=rtsp://nova:rovanova@192.168.1.53:88/videoMain ! decodebin ! videoscale ! video/x-raw ! jpegenc ! rtpjpegpay ! udpsink host=127.0.0.1 port=5002
