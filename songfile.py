
class Song:
	def __init__(self, trackid, songid, artist, title):
		self.trackid = trackid
		self.songid = songid
		self.artist = artist
		self.title = title

	def __It__ (self, other):
		if self.artist < other.artist:
			return True

	def __str__(self):
		return "%s sjunger %s" % (self.artist, self.title)



