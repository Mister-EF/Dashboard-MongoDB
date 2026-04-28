async function loadDashboard() {
    try {
        const response = await fetch('/api/data');
        const data = await response.json();
        
        const grid = document.getElementById('dashboard-grid');
        grid.innerHTML = '';

        data.forEach(item => {
            const card = `
                <div class="col-md-4 mb-4">
                    <div class="card shadow-sm">
                        <div class="card-body">
                            <h5 class="card-title">${item.title || 'Untitled'}</h5>
                            <p class="card-text">${item.description || 'No description available.'}</p>
                            <span class="badge bg-primary">Scale Factor: ${item.scale_value || 0}</span>
                        </div>
                    </div>
                </div>
            `;
            grid.innerHTML += card;
        });
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

loadDashboard();