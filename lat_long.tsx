import React, { useState } from 'react';

const GeoLocationInput = () => {
  // State to hold latitude and longitude values
  const [location, setLocation] = useState({ latitude: '', longitude: '' });

  // Function to update state based on input changes
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setLocation({
      ...location,
      [name]: parseFloat(value) // Parse input value as a float
    });
  };

  return (
    <div>
      {/* Input for latitude */}
      <div>
        <label htmlFor="latitude">Latitude:</label>
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
        <label htmlFor="longitude">Longitude:</label>
        <input
          type="number"
          id="longitude"
          name="longitude"
          value={location.longitude}
          onChange={handleInputChange}
          step="0.000001"
        />
      </div>
      
      {/* Displaying the current latitude and longitude */}
      <p>Latitude: {location.latitude || 'Not set'}, Longitude: {location.longitude || 'Not set'}</p>
    </div>
  );
};

export default GeoLocationInput;
