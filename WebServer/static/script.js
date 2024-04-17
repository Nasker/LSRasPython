window.onload = function() {
    setInterval(function() {
        fetch('/api/sensor')
            .then(response => response.json())
            .then(data => {
                document.getElementById('temperature').textContent = 'Temperature: ' + data.temperature + 'ºC';
                document.getElementById('humidity').textContent = 'Humidity: ' + data.humidity + '%';
            })
            .catch(error => console.error('Error:', error));
    }, 2000);
};

function toggleRelay() {
    fetch('/api/toggle_relay', { method: 'POST' })
        .then(response => response.text())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}