class TrafficDataRecord:
    """
    Author: Ayush Kapoor
    A class to represent a traffic data record.

    Attributes:
    ----------
    CSDUID : str
        The unique identifier for the Census Subdivision.
    CSD : str
        The name of the Census Subdivision.
    Period : int
        The year of the record.
    IndicatorSummaryDescription : str
        A description of the traffic indicator.
    UnitOfMeasure : str
        The unit of measurement.
    OriginalValue : float
        The recorded traffic value.
    """
    def __init__(self, CSDUID, CSD, Period, IndicatorSummaryDescription, UnitOfMeasure, OriginalValue):
        """
        Initializes TrafficDataRecord with provided details.

        Parameters:
        ----------
        CSDUID : str
            The unique identifier for the Census Subdivision.
        CSD : str
            The name of the Census Subdivision.
        Period : int
            The year of the record.
        IndicatorSummaryDescription : str
            A description of the traffic indicator.
        UnitOfMeasure : str
            The unit of measurement.
        OriginalValue : float
            The recorded traffic value. It will be converted to a float.
        """
        self.CSDUID = CSDUID
        self.CSD = CSD
        self.Period = Period
        self.IndicatorSummaryDescription = IndicatorSummaryDescription
        self.UnitOfMeasure = UnitOfMeasure

        # Ensure OriginalValue is a valid float
        try:
            self.OriginalValue = float(OriginalValue)
        except ValueError:
            raise ValueError(f"OriginalValue must be a float, got {type(OriginalValue)} instead")

    def __str__(self):
        """
        Returns a string representation of the traffic data record.

        Returns:
        -------
        str
            A string representation of the traffic data record.
        """
        return (f"CSDUID: {self.CSDUID}, CSD: {self.CSD}, Period: {self.Period}, "
                f"Indicator Summary: {self.IndicatorSummaryDescription}, "
                f"Unit: {self.UnitOfMeasure}, Value: {self.OriginalValue}")
