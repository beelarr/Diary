from peewee import *
import datetime

db = SqliteDatabase('diary.db')


class Entry(Model):
	content = TextField()
	timestamp = DateTimeField(default=datetime.datetime.now)

	class Meta:
		database = db

	def initialize():
		db.connect()
		db.create_tables([Entry], safe=True)

	def menu_loop():
		# Show menu

		def add_entry():
			"""Show menu"""

	def view_entries():
		"""View previous messages"""

	def delete_entry(entry):
		"""Delete an entry"""

if __name__ == '__main__':
	initialize()
	menu_loop()



