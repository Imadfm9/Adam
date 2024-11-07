from urllib.parse import urlencode

def convert_m3u8_to_dash(m3u8_url):
    # تحويل رابط m3u8 إلى رابط mpd بنمط DASH
    base_dash_url = "https://scontent.xx.fbcdn.net/hvideo-cln-odn/_nc_cat-104/_nc_sr_t-4/v/rAScg4pxjNLDJRIv2hVD2UbZGGZBlCBoBPy8I_NEr28lo-Q/_nc_ohc-U0wDZoj7KD0Q7kNvgFuux6V/live-dash/dash-abr-ibr-audio/"
    video_id = "452324134539226_0"  # يمكنك تخصيصه حسب الرابط
    params = {
        "ccb": "2-4",
        "lvp": "1",
        "ms": "m_CN",
        "p_bd": "AoKlVwZ2oTKMKtAIhJGx",
        "sc_t": "1",
        "oh": "00_AYAjJaS4ciU2K_Zg3aTdmyvd9CdrJXCR1zDuMa0IQ1xaig",
        "oe": "672469C0"
    }

    # إذا كان الرابط ينتهي بـ ".m3u8"، نحوله إلى ".mpd"
    if m3u8_url.endswith(".m3u8"):
        mpd_link = f"{base_dash_url}{video_id}.mpd?" + urlencode(params)
        return mpd_link
    else:
        print("الرابط ليس بصيغة m3u8")
        return None

# مثال على استخدام الدالة
m3u8_url = "https://live4.beinconnect.us/YallaGoalApp/beINSports1.m3u8"
mpd_link = convert_m3u8_to_dash(m3u8_url)

if mpd_link:
    print("Converted DASH link:", mpd_link)
