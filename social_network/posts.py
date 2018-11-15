from datetime import datetime
import calendar


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.user = None
        self.timestamp = datetime(2017, 1, 10)

    def set_user(self, user):
        self.user = user
        
    def __str__(self):
        return '@{name} {surname}: "Sample post text"\n\t'.format(
            name = self.user.first_name, 
            surname = self.user.last_name)
    
    def format_date(self):
        return '{}, {} {}, {}'.format(
            calendar.day_name[self.timestamp.weekday()], 
            calendar.month_name[self.timestamp.month][:3],
            self.timestamp.day,
            self.timestamp.year)


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(self.__class__, self).__init__(text)

    def __str__(self):
        return super(self.__class__, self).__str__() + self.format_date()


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(self.__class__, self).__init__(text)
        self.image_url = image_url

    def __str__(self):
         return super(self.__class__, self).__str__() + self.image_url + '\n\t' + self.format_date()


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(self.__class__, self).__init__(text)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
         return '@{name} Checked In: "Sample post text"\n\t{lat}, {lon}\n\t{date}'.format(
            name = self.user.first_name,
            lat = self.latitude,
            lon = self.longitude,
            date = self.format_date())
    
