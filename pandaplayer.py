import xbmc
from threading import Timer

class PandaPlayer(xbmc.Player):

	def __init__(self, core=None, panda=None):
		#xbmc.Player.__init__(self, xbmc.PLAYER_CORE_MPLAYER)
		#xbmc.Player.__init__(self, xbmc.PLAYER_CORE_AUTO)
		xbmc.Player.__init__(self)
		self.panda = panda
		self.timer = None

	def playSong(self, item):
		self.play(item[0], item[1])

	def play(self, url, item):
		xbmc.Player(xbmc.PLAYER_CORE_MPLAYER).play(url, item)
		#xbmc.Player(xbmc.PLAYER_CORE_AUTO).play(url, item)

	def onPlayBackStarted(self):
		print "PANDORA: onPlayBackStarted: %s" % self.getPlayingFile()
		if self.panda.playing:
			'''if not "pandora.com" in self.getPlayingFile():
				self.panda.playing = False
				self.panda.quit()
			else:
				#Show Visualization (disappears after each song...)'''
			xbmc.executebuiltin("ActivateWindow( 12006 )")

	def onPlayBackEnded(self):
		print "PANDORA: onPlayBackEnded"
		self.stop()
		print "PANDORA: playing = %s" % self.panda.playing
		if self.timer and self.timer.isAlive():
			self.timer.cancel()
		if self.panda.skip:
			self.panda.skip = False
		if self.panda.playing:
			self.timer = Timer(0.5, self.panda.playNextSong)
			self.timer.start()

	def onPlayBackStopped(self):
		print "PANDORA: onPlayBackStopped"
		self.stop()
		print "PANDORA: playing = %s" % self.panda.playing
		if self.timer and self.timer.isAlive():
			self.timer.cancel()

                #catch for if this was actually a skip
                if self.panda.playing and self.panda.skip:
                        self.panda.skip = False
                        self.timer = Timer(0.5,self.panda.playNextSong)
                        self.timer.start()
                else:
                        if xbmc.getCondVisibility('Skin.HasSetting(PandoraVis)'):
                                xbmc.executebuiltin('Skin.Reset(PandoraVis)')
                        self.panda.Quit()
		
		
