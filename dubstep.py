def song_decoder(song):
    original = song.split("WUB")
    original = [c for c in original if c != ""]
    return " ".join(original)

print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))
x = "hello"
y = x.replace('l','s')
print(y)