__author__ = 'kaniu'

class Phone():
	#encapsulation of data
	def __init__(self, serial_no, color, make):
		self.serial_no = serial_no
		self.color = color
		self.make = make


	def send_message(self):
		print('Your message is sent')

	def dial(self):
		print('please dial a number')


#showing inheritance
class SmartPhone(Phone):
	#override the parent methods
	def send_message(self):
		print('your message is being sent by a Smartphone')

	def screen_size(self, size):
		self.size = size
		print('Screen Size is: {}'.format(size))




class Tablet(Phone):
	def dial(self):
		print('your tablet is making a call')


my_phone = SmartPhone(1234, 'black', 'nokia')
print('Your Phone details are: ', my_phone.serial_no, my_phone.color, my_phone.screen_size(12))
