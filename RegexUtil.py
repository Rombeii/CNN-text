import re
from datetime import datetime, timedelta
import pycountry


class RegexUtil:
    @staticmethod
    def determine_location_type(location_part):
        try:
            # Check if it corresponds to a country
            pycountry.countries.lookup(location_part)
            return 'country'
        except LookupError:
            try:
                # Check if it corresponds to a state or province
                pycountry.subdivisions.lookup(location_part)
                return 'state'
            except LookupError:
                # Assume it corresponds to a city
                return 'city'

    @staticmethod
    def extract_location_details(location):
        parts = location.split(',')
        city = 'Unknown'
        state = 'Unknown'
        country = 'Unknown'

        if len(parts) == 1:
            # Only one part, can be city, state, or country
            location_type = RegexUtil.determine_location_type(parts[0].strip())
            if location_type == 'state':
                state = parts[0].strip()
            elif location_type == 'country':
                country = parts[0].strip()
            else:
                city = parts[0].strip()
        elif len(parts) == 2:
            # Two parts, assume it's a city and state/country
            city = parts[0].strip()
            location_type = RegexUtil.determine_location_type(parts[1].strip())
            if location_type == 'state':
                state = parts[1].strip()
            elif location_type == 'country':
                country = parts[1].strip()

        return city, state, country

    @staticmethod
    def get_location_from_text(text):
        location_regex = r"^(.*?)(?:\s+\(CNN\))"
        location_match = re.search(location_regex, text)
        location = location_match.group(1).strip() if location_match else 'Unknown'
        return RegexUtil.extract_location_details(location)

    @staticmethod
    def get_publisher_from_text(text):
        publisher_regex = r"By\s*\.\s*(.*?)\s*\.\s*PUBLISHED"
        publisher_match = re.search(publisher_regex, text)
        return publisher_match.group(1).strip() if publisher_match else 'Unknown'

    @staticmethod
    def get_date_from_text_with_regex(text, regex):
        match = re.search(regex, text)
        date_str = match.group(1).strip() if match else ''

        # Check if the date string contains "GMT"
        if "GMT" in date_str:
            date_str = date_str.replace("GMT, ", "").strip()  # Remove "GMT" from the date string
            try:
                date = datetime.strptime(date_str, "%H:%M %d %B %Y") + timedelta(hours=4)  # Add 4 hours to the time
                return date.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                return 'Unknown'
        else:
            date_str = date_str.replace("EST, ", "").strip()  # Remove "EST" from the date string
            try:
                date = datetime.strptime(date_str, "%H:%M %d %B %Y")
                return date.strftime("%Y-%m-%d %H:%M")
            except ValueError:
                return 'Unknown'
