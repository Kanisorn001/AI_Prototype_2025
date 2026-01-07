const ctx = document.getElementById('chartCanvas').getContext('2d');
const inputs = document.querySelectorAll('input');

let radarChart = new Chart(ctx, {
    type: 'radar',
    data: {
        labels: ['Sepal L', 'Sepal W', 'Petal L', 'Petal W'],
        datasets: [{
            label: 'Data',
            data: [5.1, 3.5, 1.4, 0.2],
            backgroundColor: 'rgba(142, 45, 226, 0.2)',
            borderColor: '#8e2de2',
            borderWidth: 2
        }]
    },
    options: {
        scales: { r: { beginAtZero: true, grid: { color: 'rgba(255,255,255,0.1)' }, ticks: { display: false } } },
        plugins: { legend: { display: false } }
    }
});

inputs.forEach(input => {
    input.addEventListener('input', () => {
        const values = Array.from(inputs).map(i => parseFloat(i.value) || 0);
        radarChart.data.datasets[0].data = values;
        radarChart.update();
    });
});