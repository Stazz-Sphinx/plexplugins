ART = 'artlogo.jpg'
ICON = 'icon-default.png'

NAME = 'Radio ROKS Ukraine'
NAME_AIR = 'ROKS (on the Air)'
NAME_HARD = 'ROKS (Hard and Havy)'
NAME_KAMTUGEZA = 'ROKS (KAMTUGEZA)'
NAME_CONCERT = 'ROKS (Live Concert)'
NAME_BEATLES = 'ROKS (Beatles)'
NAME_BALLADS = 'ROKS (Rock-Ballads)'


STREAM_URL_AIR = 'http://online-radioroks.tavrmedia.ua/RadioROKS'
STREAM_URL_HARD= 'http://online-radioroks2.tavrmedia.ua/RadioROKS_HardnHeavy'
STREAM_URL_KAMTUGEZA= 'http://online-radioroks2.tavrmedia.ua/RadioROKS_KAMTUGEZA'
STREAM_URL_CONCERT= 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Concert'
STREAM_URL_BEATLES= 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Beatles'
STREAM_URL_BALLADS= 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Ballads'

####################################################################################################
def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = NAME
	TrackObject.thumb = R(ICON)

####################################################################################################     
@handler('/music/radioroksukraine', NAME, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()
	oc.add(CreateTrackObject(url=STREAM_URL_AIR, title=NAME_AIR))
	oc.add(CreateTrackObject(url=STREAM_URL_HARD, title=NAME_HARD))
	oc.add(CreateTrackObject(url=STREAM_URL_KAMTUGEZA, title=NAME_KAMTUGEZA))
	oc.add(CreateTrackObject(url=STREAM_URL_CONCERT, title=NAME_CONCERT))
	oc.add(CreateTrackObject(url=STREAM_URL_BEATLES, title=NAME_BEATLES))
	oc.add(CreateTrackObject(url=STREAM_URL_BALLADS, title=NAME_BALLADS))

	return oc

####################################################################################################
def CreateTrackObject(url, title, include_container=False):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, include_container=True),
		rating_key = url,
		title = title,
		items = [
			MediaObject(
				parts = [
					PartObject(key=Callback(PlayAudio, url=url, ext='mp3'))
				],
				container = Container.MP3,
				bitrate = 128,
				audio_codec = AudioCodec.MP3,
				audio_channels = 2
			)
		]
	)

	if include_container:
		return ObjectContainer(objects=[track_object])
	else:
		return track_object

####################################################################################################
def PlayAudio(url):

	return Redirect(url)
