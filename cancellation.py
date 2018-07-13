#Cancellation Module

class Cancellation:
	def __init__(self,cancellationid,bookingid,cancellationdate):
		self.__cancellationid=cancellationid
		self.__bookingid=bookingid
		self.cancellationdate=cancellationdate

	def SetCancellationId(self,cancellationid):
		self.__cancellationid=cancellationid

	def SetBookingId(self,bookingid):
		self.__bookingid=bookingid

	def SetCancellationDate(self,cancellationdate):
		self.cancellationdate=cancellationdate

	def GetCancellationId(self):
		return self.__cancellationid

	def GetBookingId(self):
		return self.__bookingid

	def GetCancellationDate(self):
		return self.__cancellationdate

