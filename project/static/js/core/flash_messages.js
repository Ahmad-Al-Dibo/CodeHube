document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll('.flash-message');
    messages.forEach(msg => {
        // Na 3 seconden starten fade
        setTimeout(() => {
            msg.style.opacity = "0";
            msg.style.transform = "translateY(-20px)";
            // Na overgang verwijderen uit DOM
            setTimeout(() => msg.remove(), 500); 
        }, 3000); // 3 seconden zichtbaar
    });
});