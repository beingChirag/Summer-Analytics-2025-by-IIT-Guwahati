// =====================
// FAQ Accordion Toggle
// =====================
const accordions = document.querySelectorAll('.FAQ__accordian');

accordions.forEach(acc => {
    const btn = acc.querySelector('.FAQ__title');
    const content = acc.querySelector('.FAQ__visible');

    btn.addEventListener('click', () => {
        const isOpen = content.style.maxHeight && content.style.maxHeight !== '0px';

        // Close all other open accordions
        document.querySelectorAll('.FAQ__visible').forEach(el => {
            el.style.maxHeight = null;
        });
        document.querySelectorAll('.FAQ__title i').forEach(icon => {
            icon.classList.remove('fa-times');
            icon.classList.add('fa-plus');
        });

        if (!isOpen) {
            content.style.maxHeight = content.scrollHeight + 'px';
            btn.querySelector('i').classList.remove('fa-plus');
            btn.querySelector('i').classList.add('fa-times');
        }
    });
});

// =====================
// Email Input Label Animation
// =====================
const emailInputs = document.querySelectorAll('.email__input');

emailInputs.forEach(input => {
    input.addEventListener('focus', () => {
        input.nextElementSibling.style.top = '0.2rem';
        input.nextElementSibling.style.fontSize = '10px';
    });

    input.addEventListener('blur', () => {
        if (!input.value) {
            input.nextElementSibling.style.top = '28%';
            input.nextElementSibling.style.fontSize = '16px';
        }
    });
});

// =====================
// Language Dropdown - Log selected language
// (Optional Feature)
// =====================
const languageSelect = document.querySelectorAll('#languagesSelect');
languageSelect.forEach(select => {
    select.addEventListener('change', (e) => {
        console.log(`Language changed to: ${e.target.value}`);
    });
});