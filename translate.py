class day:
	def __init__(self, day):
		if day == "Sun": # Sunday
			self.day = "Dom"

		elif day == "Mon": # Monday
                        self.day = "Seg"

		elif day == "Tue": # Tuesday
                        self.day = "Ter"

		elif day == "Wed": # Wednesday
                        self.day = "Qua"

		elif day == "Thu": # Thursday
                        self.day = "Qui"

		elif day == "Fri": # Friday
                        self.day = "Sex"

		elif day == "Sat": # Saturday
			self.day = "sab"

class month:
	def __init__(self, month):
		if month == "Jan": # January
			self.month = "Jan"

		elif month == "Feb": # February
        		self.month = "Fev"

		elif month == "Mar": # March
		        self.month = "Mar"

		elif month == "Apr": # April
		        self.month = "Abr"

		elif month == "May": # May
		        self.month = "Mai"

		elif month == "Jun": # June
        		self.month = "Jun"

		elif month == "Jul": # July
		        self.month = "Jul"

		elif month == "Aug": # August
		        self.month = "Ago"

		elif month == "Sep": # September
		        self.month = "Set"

		elif month == "Oct": # October
		        self.month = "Out"

		elif month == "Nov": # November
		        self.month = "Nov"

		elif month == "Dec": # December
		        self.month = "Dez"
