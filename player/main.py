import mpv

player = mpv.MPV(ytdl=True, input_default_bindings=True, input_vo_keyboard=True)
player.play('https://www.youtube.com/watch?v=dQw4w9WgXcQ')