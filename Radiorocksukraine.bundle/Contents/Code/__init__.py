ART = 'artlogo.jpg'
ICON = 'icon-default.png'
ICON_OE = 'icon-oe.jpg'
ICON_ACDC = 'icon-acdc.jpg'
ICON_THE_BEATLES = 'icon-thebeatles.jpg'
ICON_SCORPIONS = 'icon-scorpions.jpg'
ICON_UAROCK = 'icon-uarock.jpg'

NAME = 'Radio ROKS Ukraine'
NAME_AIR = 'ROKS (on Air)'
NAME_ACDC= 'ROKS (AC/DC)'
NAME_HARD = 'ROKS (Hard and Havy)'
NAME_KAMTUGEZA = 'ROKS [KAMTYГЕЗA]'
NAME_CONCERT = 'ROKS (Live Concert)'
NAME_BEATLES = 'ROKS (Beatles)'
NAME_SCORPIONS = 'ROKS (Scorpions)'
NAME_BALLADS = 'ROKS (Rock-Ballads)'
NAME_UKRROCK = 'ROKS (Ukraine ROCK)'
NAME_NEWROCK = 'ROKS (NEW ROCK)'
NAME_OE = 'ROKS (Okean Elzy) '

STREAM_URL_ACDC = 'http://online-radioroks2.tavrmedia.ua:7000/RadioROKS_ACDC'
STREAM_URL_AIR = 'http://online-radioroks.tavrmedia.ua/RadioROKS'
STREAM_URL_HARD = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_HardnHeavy'
STREAM_URL_KAMTUGEZA = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_KAMTUGEZA'
STREAM_URL_CONCERT = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Concert'
STREAM_URL_BALLADS = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Ballads'
STREAM_URL_BEATLES = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Beatles'
STREAM_URL_SCORPIONS = 'http://online-radioroks2.tavrmedia.ua:7000/RadioROKS_Scorpions'
STREAM_URL_UKRROCK = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_Ukr'
STREAM_URL_NEWROCK = 'http://online-radioroks2.tavrmedia.ua/RadioROKS_NewRock'
STREAM_URL_OE = 'http://online-radioroks2.tavrmedia.ua:7000/RadioROKS_OE' 

####################################################################################################
def Start():

	ObjectContainer.art = R(ART)
	ObjectContainer.title1 = NAME
	TrackObject.thumb = R(ICON)

####################################################################################################     
@handler('/music/radioroksukraine', NAME, thumb=ICON, art=ART)
def MainMenu():

	oc = ObjectContainer()

	oc.add(CreateTrackObject(url=STREAM_URL_AIR, title=NAME_AIR, thumb=R(ICON)))
	oc.add(CreateTrackObject(url=STREAM_URL_HARD, title=NAME_HARD, thumb=R(ICON)))
	oc.add(CreateTrackObject(url=STREAM_URL_KAMTUGEZA, title=NAME_KAMTUGEZA, thumb=R(ICON)))
	oc.add(CreateTrackObject(url=STREAM_URL_CONCERT, title=NAME_CONCERT, thumb=R(ICON)))
	oc.add(CreateTrackObject(url=STREAM_URL_ACDC, title=NAME_ACDC, thumb=R(ICON_ACDC)))
	oc.add(CreateTrackObject(url=STREAM_URL_BEATLES, title=NAME_BEATLES, thumb=R(ICON_THE_BEATLES)))
	oc.add(CreateTrackObject(url=STREAM_URL_OE, title=NAME_OE, thumb=R(ICON_OE)))
	oc.add(CreateTrackObject(url=STREAM_URL_SCORPIONS, title=NAME_SCORPIONS, thumb=R(ICON_SCORPIONS)))
	oc.add(CreateTrackObject(url=STREAM_URL_BALLADS, title=NAME_BALLADS, thumb=R(ICON)))
	oc.add(CreateTrackObject(url=STREAM_URL_UKRROCK, title=NAME_UKRROCK, thumb=R(ICON_UAROCK)))
	oc.add(CreateTrackObject(url=STREAM_URL_NEWROCK, title=NAME_NEWROCK, thumb=R(ICON) ))

	return oc

####################################################################################################
def CreateTrackObject(url, title, thumb, include_container=False):

	track_object = TrackObject(
		key = Callback(CreateTrackObject, url=url, title=title, thumb=thumb, include_container=True),
		rating_key = url,
		title = title,
		thumb = thumb,
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
