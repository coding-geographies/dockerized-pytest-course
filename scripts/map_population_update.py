class MapData():
    def __init__(self, data, updated):
        self._data = data
        if updated:  # if this value is True
            if self.updated_population_count():
                self._updated = updated
            else:
                self._updated = False


    def get_data(self):
        """
        Returns:
        list: Data object that is a list of dictionaries
        """
        return self._data


    def updated_population_count(self):
        """
        This validates whether the data has been updated with the 'Population'
        and 'Updated' column per row.

        Returns:
        boolean: Check whether the list has been updated (true) or not (false)
        """
        for row in self._data:
            if 'Population' not in row.keys() or 'Updated' not in row.keys():
                return False
        return True


    def add_population(self, pop_map):
        """
        If the data has not been updated, this function cross-references
        a dictionary containing countries and their respective populations.
        Using this information, it updates each row entry to include
        the population for the country it represents.

        Parameters:
        pop_map (dict): Dictionary of countries and their populations
        self._data(list): List of row objects (represented as OrderedDicts)

        Returns:
         None
        """
        if not self.updated_population_count():
            for row in self._data:
                if row['Country'] in pop_map.keys():
                    row['Population'] = pop_map[row['Country']]
                else:
                    row['Population'] = None
                row['Updated'] = True
        else:
            raise Exception('You cannot transform the data twice')
