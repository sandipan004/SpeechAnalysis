document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('analyze-form');
    const input = document.getElementById('text-input');
    const submitBtn = document.getElementById('submit-btn');
    const btnText = document.querySelector('.btn-text');
    const loader = document.querySelector('.loader');
    const resultsSection = document.getElementById('results-section');
    const metricsContainer = document.getElementById('metrics-container');
    const overallStatus = document.getElementById('overall-status');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        
        const text = input.value.trim();
        if (!text) return;

        // Set Loading State
        submitBtn.disabled = true;
        btnText.classList.add('hidden');
        loader.classList.remove('hidden');
        resultsSection.classList.add('hidden');

        try {
            const response = await fetch('/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ text: text })
            });

            if (!response.ok) {
                throw new Error(`API error: ${response.status}`);
            }

            const data = await response.json();
            renderResults(data);

        } catch (error) {
            console.error('Failed to analyze text:', error);
            alert('An error occurred while analyzing the text. Please ensure the backend is running.');
        } finally {
            // Remove Loading State
            submitBtn.disabled = false;
            btnText.classList.remove('hidden');
            loader.classList.add('hidden');
        }
    });

    function renderResults(data) {
        metricsContainer.innerHTML = '';
        let isToxic = false;

        Object.entries(data).forEach(([key, probability]) => {
            const percentage = Math.round(probability * 100);
            if (percentage > 50) isToxic = true;
            
            const labelName = key.replace('_', ' ').replace(/\b\w/g, l => l.toUpperCase());
            const dangerClass = percentage > 50 ? 'danger' : '';

            const metricHtml = `
                <div class="metric-item">
                    <div class="metric-header">
                        <span class="metric-label">${labelName}</span>
                        <span class="metric-value">${percentage}%</span>
                    </div>
                    <div class="progress-bar-bg">
                        <div class="progress-bar-fill ${dangerClass}" style="width: 0%"></div>
                    </div>
                </div>
            `;
            metricsContainer.insertAdjacentHTML('beforeend', metricHtml);
        });

        // Update overall status badge
        overallStatus.className = 'status-badge ' + (isToxic ? 'status-toxic' : 'status-safe');
        overallStatus.textContent = isToxic ? 'Toxicity Detected' : 'Content Safe';

        // Show results section
        resultsSection.classList.remove('hidden');

        // Trigger animations
        requestAnimationFrame(() => {
            const progressBars = document.querySelectorAll('.progress-bar-fill');
            Object.values(data).forEach((probability, index) => {
                const percentage = Math.round(probability * 100);
                // Slight delay for stagger effect
                setTimeout(() => {
                    progressBars[index].style.width = `${percentage}%`;
                }, index * 100);
            });
        });
    }
});
