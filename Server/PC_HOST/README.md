# README
# Configure PC as wfi router
It is onmy necessary if you chose to run the host on your laptop. Else you can check you the RPI instruction.

## Install the request package
Run the programme `install_request.sh`.

## Confi
Edit the file `/etc/hostapd/hostapd.conf`
```
interface=wlan0
ssid=JDR_Game
hw_mode=g
channel=7
wmm_enabled=0
auth_algs=1
wpa=2
wpa_passphrase=monpassword
wpa_key_mgmt=WPA-PSK
rsn_pairwise=CCMP
```

## Run the modifiation 
`sudo systemctl start hostapd`
