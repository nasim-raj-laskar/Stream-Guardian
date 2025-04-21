document.addEventListener('DOMContentLoaded', function () {
    const socket = io();
    let allMessages = [];

    //Charts
    const ratioChart = new ApexCharts(document.querySelector("#ratioChart"), {
        series: [0, 0],
        chart: {
            type: 'donut',
            height: 350
        },
        labels: ['Clean', 'Toxic'],
        colors: ['#5cb85c', '#d64045'],
        legend: {
            position: 'bottom'
        },
        responsive: [{
            breakpoint: 480,
            options: {
                chart: {
                    width: 200
                },
                legend: {
                    position: 'bottom'
                }
            }
        }]
    });
    ratioChart.render();

    const trendChart = new ApexCharts(document.querySelector("#trendChart"), {
        series: [{
            name: "Toxic Messages",
            data: []
        }],
        chart: {
            type: 'line',
            height: 350,
            animations: {
                enabled: true
            }
        },
        stroke: {
            curve: 'smooth',
            width: 3,
            colors: ['#d64045']
        },
        xaxis: {
            categories: Array.from({ length: 10 }, (_, i) => `${i + 1} min ago`).reverse()
        },
        tooltip: {
            enabled: true
        }
    });
    trendChart.render();

    //Filter buttons
    const filterButtons = document.querySelectorAll('.filter-controls button');
    filterButtons.forEach(button => {
        button.addEventListener('click', function () {
            filterButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            filterMessages(this.id.replace('show-', ''));
        });
    });
    document.getElementById('message-search').addEventListener('input', function () {
        const searchTerm = this.value.toLowerCase();
        const messages = document.querySelectorAll('.message');

        messages.forEach(message => {
            const text = message.querySelector('.content').textContent.toLowerCase();
            if (text.includes(searchTerm)) {
                message.classList.add('highlight');
                message.style.display = 'block';
            } else {
                message.classList.remove('highlight');
                if (document.querySelector('.filter-controls button.active').id !== 'show-all') {
                    message.style.display = 'none';
                }
            }
        });
    });

    //messages
    function filterMessages(filter) {
        const messages = document.querySelectorAll('.message');
        const searchTerm = document.getElementById('message-search').value.toLowerCase();

        messages.forEach(message => {
            const isToxic = message.classList.contains('toxic');
            const text = message.querySelector('.content').textContent.toLowerCase();
            const matchesSearch = searchTerm === '' || text.includes(searchTerm);

            if (filter === 'all' && matchesSearch) {
                message.style.display = 'block';
            } else if (filter === 'clean' && !isToxic && matchesSearch) {
                message.style.display = 'block';
            } else if (filter === 'toxic' && isToxic && matchesSearch) {
                message.style.display = 'block';
            } else {
                message.style.display = 'none';
            }
            if (searchTerm && !text.includes(searchTerm)) {
                message.classList.remove('highlight');
            }
        });
    }

    //Socket.IO event listeners
    socket.on('update', function (data) {
        document.getElementById('total-count').textContent = data.stats.total;
        document.getElementById('clean-count').textContent = data.stats.clean;
        document.getElementById('toxic-count').textContent = data.stats.toxic;
        document.getElementById('toxic-per-minute').textContent = data.stats.toxic_per_minute || 0;

        const toxicityRate = data.stats.total > 0
            ? Math.round((data.stats.toxic / data.stats.total) * 100)
            : 0;
        document.getElementById('toxicity-rate').textContent = toxicityRate + '%';

        ratioChart.updateSeries([data.stats.clean, data.stats.toxic]);

        if (data.stats.toxic_trend && data.stats.toxic_trend.length > 0) {
            trendChart.updateSeries([{
                data: data.stats.toxic_trend
            }]);
        }

        //alert banner
        if (data.newMessage.verdict === 'toxic') {
            const alertBanner = document.getElementById('toxic-alert');
            document.getElementById('alert-text').textContent = `Toxic comment detected: "${data.newMessage.text}"`;
            document.getElementById('alert-time').textContent = data.newMessage.timestamp;
            alertBanner.style.display = 'block';
            setTimeout(() => {
                alertBanner.style.display = 'none';
            }, 10000);
        }
        if (data.newMessage) {
            addMessageToWindow(data.newMessage);
            allMessages.push(data.newMessage);
        }
    });

    function addMessageToWindow(message) {
        const messagesWindow = document.getElementById('messages-window');
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${message.verdict === 'toxic' ? 'toxic' : 'clean'}`;

        messageDiv.innerHTML = `
            <div class="timestamp">${message.timestamp}</div>
            <div class="content">${message.text}</div>
            <div class="status">${message.type}</div>
        `;

        if (messagesWindow.firstChild) {
            messagesWindow.insertBefore(messageDiv, messagesWindow.firstChild);
        } else {
            messagesWindow.appendChild(messageDiv);
        }

        
        if (messagesWindow.scrollTop === 0) {
            messagesWindow.scrollTop = 0;
        }

       
        const activeFilter = document.querySelector('.filter-controls button.active').id.replace('show-', '');
        filterMessages(activeFilter);
    }
});