// static/js/enhance.js
// Modern UI enhancements for your Todo app

document.addEventListener('DOMContentLoaded', function() {
    // --- Random App Name ---
    const appNames = [
        'TodoVerse', 'TodoVerse'
    ];
    const brand = document.querySelector('.navbar-brand');
    if (brand) {
        const randomName = appNames[Math.floor(Math.random() * appNames.length)];
        brand.textContent = randomName;
        brand.style.transition = 'color 0.5s, letter-spacing 0.5s';
        brand.addEventListener('mouseover', () => {
            brand.style.color = '#6f42c1';
            brand.style.letterSpacing = '2px';
        });
        brand.addEventListener('mouseout', () => {
            brand.style.color = '';
            brand.style.letterSpacing = '';
        });
    }

    // --- Dark Mode Toggle ---
    const darkToggle = document.createElement('button');
    darkToggle.textContent = '🌙';
    darkToggle.className = 'btn btn-outline-dark ms-2';
    darkToggle.style.position = 'fixed';
    darkToggle.style.top = '16px';
    darkToggle.style.right = '16px';
    darkToggle.style.zIndex = '999';
    document.body.appendChild(darkToggle);
    darkToggle.addEventListener('click', () => {
        document.body.classList.toggle('dark-mode');
        if (document.body.classList.contains('dark-mode')) {
            darkToggle.textContent = '☀️';
        } else {
            darkToggle.textContent = '🌙';
        }
    });

    // --- Add dark mode styles ---
    const darkStyle = document.createElement('style');
    darkStyle.textContent = `
        body.dark-mode {
            background: #181a1b !important;
            color: #e4e6eb !important;
        }
        body.dark-mode .navbar, body.dark-mode .table {
            background: #23272b !important;
            color: #e4e6eb !important;
        }
        body.dark-mode .form-control, body.dark-mode .btn {
            background: #23272b !important;
            color: #e4e6eb !important;
            border-color: #444;
        }
        body.dark-mode .btn-dark {
            background: #6f42c1 !important;
            color: #fff !important;
        }
        body.dark-mode .btn-danger {
            background: #e74c3c !important;
        }
        body.dark-mode .btn-primary {
            background: #3498db !important;
        }
        body.dark-mode .table th, body.dark-mode .table td {
            border-color: #444 !important;
        }
    `;
    document.head.appendChild(darkStyle);

    // --- Ripple effect for buttons ---
    document.querySelectorAll('.btn').forEach(btn => {
        btn.style.position = 'relative';
        btn.addEventListener('click', function(e) {
            const ripple = document.createElement('span');
            ripple.className = 'ripple';
            ripple.style.position = 'absolute';
            ripple.style.background = 'rgba(111,66,193,0.3)';
            ripple.style.borderRadius = '50%';
            ripple.style.pointerEvents = 'none';
            ripple.style.width = ripple.style.height = Math.max(btn.offsetWidth, btn.offsetHeight) + 'px';
            ripple.style.left = (e.offsetX - btn.offsetWidth/2) + 'px';
            ripple.style.top = (e.offsetY - btn.offsetHeight/2) + 'px';
            ripple.style.transform = 'scale(0)';
            ripple.style.transition = 'transform 0.5s, opacity 0.5s';
            btn.appendChild(ripple);
            setTimeout(() => {
                ripple.style.transform = 'scale(1)';
                ripple.style.opacity = '0';
            }, 10);
            setTimeout(() => {
                ripple.remove();
            }, 510);
        });
    });

    // --- Toast notification ---
    function showToast(msg) {
        const toast = document.createElement('div');
        toast.textContent = msg;
        toast.style.position = 'fixed';
        toast.style.bottom = '32px';
        toast.style.right = '32px';
        toast.style.background = '#6f42c1';
        toast.style.color = '#fff';
        toast.style.padding = '12px 24px';
        toast.style.borderRadius = '8px';
        toast.style.boxShadow = '0 2px 8px rgba(0,0,0,0.15)';
        toast.style.zIndex = '1000';
        toast.style.fontSize = '1.1rem';
        document.body.appendChild(toast);
        setTimeout(() => toast.remove(), 2200);
    }

    // Show toast on Add/Update/Delete button click
    document.querySelectorAll('.btn-dark, .btn-primary, .btn-danger').forEach(btn => {
        btn.addEventListener('click', function() {
            if (btn.classList.contains('btn-dark')) showToast('Todo Added!');
            if (btn.classList.contains('btn-primary')) showToast('Todo Updated!');
            if (btn.classList.contains('btn-danger')) showToast('Todo Deleted!');
        });
    });

    // --- Animate table rows on hover ---
    document.querySelectorAll('table.table tbody tr').forEach(row => {
        row.style.transition = 'background 0.3s, box-shadow 0.3s';
        row.addEventListener('mouseover', () => {
            row.style.backgroundColor = '#f3e8ff';
            row.style.boxShadow = '0 2px 8px rgba(111,66,193,0.08)';
        });
        row.addEventListener('mouseout', () => {
            row.style.backgroundColor = '';
            row.style.boxShadow = '';
        });
    });

    // --- Highlight current page in navbar ---
    document.querySelectorAll('.nav-link').forEach(link => {
        if (window.location.pathname === '/' && link.textContent.trim() === 'Home') {
            link.classList.add('fw-bold', 'text-primary');
        }
    });
});
