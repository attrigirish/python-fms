#Booking Module

class Booking:
	def __init__(self,bookingid,userid,flightno,bookingdate):
		self.__bookingid=bookingid
		self.__userid=userid
		self.__flightno=flightno
		self.__bookingdate=bookingdate

	def SetBookingId(self,bookingid):
		self.__bookingid=bookingid

	def SetUserId(self,userid):
		self.__userid=userid

	def SetFlightNo(self,flightno):
		self.__flightno=flightno

	def SetBookingDate(self,bookingdate):
		self.__bookingdate=bookingdate

	def GetBookingId(self):
		return self.__bookingid

	def GetUserId(self):
		return self.__userid

	def GetFlightNo(self):
		return self.__flightno

	def GetBookingDate(self):
		return self.__bookingdate