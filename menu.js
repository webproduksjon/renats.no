(() => {
  const button = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#site-navigation');
  if (!button || !nav) return;

  const setOpen = (open) => {
    button.setAttribute('aria-expanded', String(open));
    nav.classList.toggle('is-open', open);
    button.textContent = open ? 'Lukk meny' : 'Meny';
  };

  button.addEventListener('click', () => {
    setOpen(button.getAttribute('aria-expanded') !== 'true');
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      setOpen(false);
      button.focus();
    }
  });
})();
