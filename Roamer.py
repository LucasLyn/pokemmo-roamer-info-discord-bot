from init import (month_names,
                  current_month)

class Roamer:
    def __init__(self,
                 name:str,
                 region:str,
                 avail_months:list[int],
                 avail_locations:list[str]):
        self.name = name
        self.region = region
        self.avail_months = avail_months
        self.avail_locations = avail_locations
    

    def is_available(self,
                     month:int
                     ) -> bool:
        '''
        Checks if the roamer is available in a given month.

        ### Parameters:
        - month (int):
            The given month to check availability for.
        
        ### Returns:
            A bool corresponding to whether or not the roamer is available in the given
        '''
        return month in self.avail_months
    

    def get_avail_months(self,
                         months:list[str]
                         )-> str:
        '''
        Gets a string of the name of months the roamer is available in.

        ### Parameters:
        - months (list):
            All month names to pick from.
        
        ### Returns:
            A string with all the month names the roamer is available in.
            String format: MONTH_NAME1, MONTH_NAME2, ..., MONTH_NAMEn
        '''
        ret_str = ''

        for month in self.avail_months:
            ret_str += months[month]

            if month != self.avail_months[-1]:
                ret_str += ", "
        
        return ret_str
    

    def get_avail_locations(self)-> str:
        '''
        Gets a string of locations where the roamer can be found.

        ### Returns:
            A string with all the locations the roamer can be found in.
            String format: LOC1, LOC2, ..., LOCn
        '''
        ret_str = ''

        for location in self.avail_locations:
            ret_str += location

            if location is not self.avail_locations[-1]:
                ret_str += ", "
        
        return ret_str


    def __str__(self) -> str:
        return ''.join([
               f"## {self.name}:\n",
               f"Region: {self.region}\n",
               f"Can be found outdoors in: {self.get_avail_locations()}\n",
               f"Available months: {self.get_avail_months(month_names)}\n",
               f"Currently available: {self.is_available(current_month)}\n"])
