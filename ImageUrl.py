class ImageUrl:

	def __init__(self):
		self.LOG_TAG = "ImageUrl: "
		
	def getImageUrl(self, level, charge):
		strlevel = str(level)
		print(self.LOG_TAG + strlevel)
		if "charge" in charge:
			urlFirstPart = "background: url('res/ic_battery_charging_"
		else:
			urlFirstPart = "background: url('res/ic_battery_"

		urlSecondPart = "_black_24dp.png') no-repeat center; border: none"
		if 0 < level <= 30:
			url = urlFirstPart + "20" + urlSecondPart
		elif 30 < level <= 50:
			url = urlFirstPart + "30" + urlSecondPart
		elif 50 < level <= 60:
			url = urlFirstPart + "50" + urlSecondPart
		elif 60 < level <= 80:
			url = urlFirstPart + "60" + urlSecondPart
		elif 80 < level <= 90:
			url = urlFirstPart + "80" + urlSecondPart
		elif 90 < level < 100:
			url = urlFirstPart + "90" + urlSecondPart
		elif level == 100:
			url = urlFirstPart + "full" + urlSecondPart

		print(self.LOG_TAG + url)
		return url

if __name__ == "__main__":
	img = ImageUrl()
	img.getImageUrl(35, "evaluation")