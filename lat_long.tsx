import React, { useState } from 'react';

const GeoLocationInput = () => {
  // State to hold latitude, longitude, date, and scale values
  const [location, setLocation] = useState({
    latitude: '',
    longitude: '',
    date: '',
    scale: 0.10
  });

  // Function to update state based on input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setLocation({
      ...location,
      [name]: name === 'scale' ? parseFloat(value) : value // Parse scale as float
    });
  };

  return (
    <div>
      {/* Input for latitude */}
      <div>
        <label htmlFor="latitude">Latitude (float):</label>
        <input
          type="number"
          id="latitude"
          name="latitude"
          value={location.latitude}
          onChange={handleInputChange}
          step="0.000001"
        />
      </div>
      
      {/* Input for longitude */}
      <div>
        <label htmlFor="longitude">Longitude (float):</label>
        <input
          type="number"
          id="longitude"
          name="longitude"
          value={location.longitude}
          onChange={handleInputChange}
          step="0.000001"
        />
      </div>

      {/* Input for date */}
      <div>
        <label htmlFor="date">Date (YYYY-MM-DD):</label>
        <input
          type="text"
          id="date"
          name="date"
          value={location.date}
          onChange={handleInputChange}
        />
      </div>

      {/* Input for scale */}
      <div>
        <label htmlFor="scale">Scale (float in degrees, default 0.10):</label>
        <input
          type="number"
          id="scale"
          name="scale"
          value={location.scale}
          onChange={handleInputChange}
          step="0.01"
        />
      </div>
      
      {/* Displaying the current latitude, longitude, date, and scale */}
      <p>Latitude: {location.latitude || 'Not set'}, Longitude: {location.longitude || 'Not set'}, Date: {location.date || 'Not set'}, Scale: {location.scale}</p>
    </div>
  );
};

export default GeoLocationInput;
